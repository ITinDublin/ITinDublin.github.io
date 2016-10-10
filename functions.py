#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import sys
import json
import glob
import unicodedata
import requests
import shutil
import posixpath
import random
import logging
import hashlib
import functools
import os

from collections import defaultdict
from copy import copy
from bs4 import BeautifulSoup
from pelican import settings
from pelican.readers import MarkdownReader, RstReader


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii


class TagWiki:
    """
    Classe responsável por criar o índice de  tags da wiki,
    permitindo assim a criação das páginas da wiki referente a cada tag.
    """
    def __init__(self, file_reader):
        self.file_reader = file_reader
        self.tag_index = defaultdict(list)

    @staticmethod
    def _transform_page_tag_wiki(path, tag, values):
        """
        Edita o html para mostrar apenas as páginas referente a tag recebida.
        :param path: (string) local do arquivo
        :param tag: (string) Tag consultada
        :param values: (dict) páginas referentes a tag. ex: {'url':'#', 'titulo': 'title'}
        :return: html
        """
        soup = BeautifulSoup(open(path), 'html.parser')
        extract_div = soup.find(id="wiki-list").extract()
        wiki_content = soup.find(id="wiki-content")
        wiki_content.contents = []
        for value in values:
            copy_div = copy(extract_div)
            copy_div.div.a.string = value['titulo']
            copy_div.div.a['href'] = "/"+value['url']
            copy_div.find("div", {"class": "tag-wiki"}).extract()
            wiki_content.append(copy_div)
            wiki_content.append(soup.new_tag("hr"))

        title = "Resuldados para tag: {}".format(str(tag))
        breadcrumb = soup.find("ul", {"class": "breadcrumb"})
        breadcrumb.findAll('li')[2].extract()
        for label, link in [('Tags', "/wiki/tags"), (title, '#')]:
            li = copy(breadcrumb.findAll('li')[1])
            li.a.string = label
            li.a['href'] = link
            breadcrumb.append(li)

        soup.title.string = title
        soup.find(id='title-wiki').string = title
        return soup.prettify()

    def _tag_wiki_make_dir(self, default_path='output/wiki/tags'):
        """Monta o path para cada tag."""
        for tag, values in self.tag_index.items():
            tag = str(remove_accents(tag), 'utf-8')
            file_path = os.path.join(copy(default_path), "/".join([tag, 'index.html']))
            try:
                os.makedirs(os.path.dirname(file_path))
            except FileExistsError:
                pass

            path_for_cp = [
                ('output/wiki.html', 'output/wiki/index.html'),
                ('output/tags-wiki.html', 'output/wiki/tags/index.html'),
                ('output/resultados.html', file_path)
            ]
            for file1, file2 in path_for_cp:
                shutil.copy2(file1, file2)

            content = self._transform_page_tag_wiki(file_path, tag, values)

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

            logging.info('Writing %s', file_path)

    def create_index_tags(self, make_dir=True):
        for file_name, titulo, tags in self.file_reader:
            for tag in tags:
                self.tag_index[str(tag)].append({'url': file_name, 'titulo': titulo})
        if make_dir:
            self._tag_wiki_make_dir()


def tags_wiki_generator(make_dir=True):
    """
    Cria o índice de tags e constroi o diretório  se make_dir=True
    senão só cria o indice.
    :return: list of dict [{'tag': [{'url': '#', 'titulo': 'titulo'}]}]
    """
    tag_wiki = TagWiki(reader_wiki_files())
    tag_wiki.create_index_tags(make_dir)
    return tag_wiki.tag_index


def reader_wiki_files():
    """
    Faz a leitura das páginas da wiki para poder pegar o título as tags e o nome do arquivo
    que irá ser utilizado para montar a página de listagem, e as páginas para cada tag encontrada.
    :return:
    """
    reader = {
        'rst': RstReader(settings.DEFAULT_CONFIG),
        'md': MarkdownReader(settings.DEFAULT_CONFIG),
    }

    path_wiki = 'content/pages/wiki/'

    wiki_pages = []
    for file in os.listdir(path_wiki):
        file_name, extensao = file.split(".")
        if extensao not in reader.keys():
            raise Exception('Extensão do arquivo inválida')

        metadata = reader[extensao].read(path_wiki+file)[1]
        tags = metadata.get('tags', [])
        title = metadata.get('title')
        wiki_pages.append((file_name, title, tags))

    return wiki_pages


def get_wiki_pages():
    """Lista de páginas da wiki"""
    return reader_wiki_files()


def get_tags_wiki():
    """Lista de tags nas páginas da wiki"""
    tags_wiki = tags_wiki_generator(False)
    return tags_wiki.keys()


def get_avatar(autor, membros):
    if autor not in membros or \
            not any([True for key in membros[autor].keys() if key in ['github', 'email', 'twitter']]):
        return "/theme/img/{}".format("default_avatar.gif")

    link_img = {
        'github': "https://avatars.githubusercontent.com/{}?size=250",
        'email': "http://www.gravatar.com/avatar/{}?s=250",
        'twitter': "http://avatars.io/twitter/{}",
    }
    url_img = None
    for account, username in membros['autor'].items():
        url_img = link_img.get(account)
        if url_img:
            if account == 'email':
                username = hashlib.md5(membros[autor]['email'].strip().lower().encode("utf-8")).hexdigest()
            else:
                username = username[1:] if username.startswith("@") else username
            break

    if not url_img:
        return "/theme/img/{}".format("default_avatar.gif")

    return url_img.format(username)


def get_article_image(article, root):
    if hasattr(article, 'image'):
        img = article.image
        return img[1:] if img.startswith('/') else img

    if not root:
        return ""

    base = os.path.join('content', root)
    banners = map(functools.partial(os.path.join, root), os.walk(base).next()[2])
    random.seed(article.date)
    return random.choice(banners)


def get_article_at_github(article, repo, branch):
    base = posixpath.relpath(article.source_path, os.getcwd())
    return posixpath.join(repo, 'tree/', branch, base)


def get_link(link):
    return link if link.startswith('http://') or link.startswith('https://') else '/' + link


def get_groups_meetup(path):
    meetups = [json.load(open(fname, 'r', encoding='utf-8')) for fname in glob.glob(path)]
    return meetups[0].keys()


def clear_cache_event_group_meetup(api_service):
    url = "{}/clear_all_caches".format(api_service)
    requests.request("POST", url)


if __name__ == '__main__':
    func_name = sys.argv[1]
    if func_name == 'tags_generator':
        tags_wiki_generator()
