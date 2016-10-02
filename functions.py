#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import sys
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
            file_path = os.path.join(copy(default_path), "/".join([tag, 'index.html']))
            try:
                os.makedirs(os.path.dirname(file_path))
            except FileExistsError:
                pass

            path_for_cp = [
                ('output/wiki.html', 'output/wiki/index.html'),
                ('output/tags-wiki.html', 'output/wiki/tags/index.html'),
                ('output/wiki.html', file_path)
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
    md_reader = MarkdownReader(settings.DEFAULT_CONFIG)
    rst_reader = RstReader(settings.DEFAULT_CONFIG)

    content = 'content/pages/wiki/'

    wiki_pages = []
    for page in os.listdir(content):
        file_name, extensao = page.split(".")
        if extensao == 'rst':
            metadata = rst_reader.read(content+page)[1]
        else:
            metadata = md_reader.read(content+page)[1]
        tags = metadata.get('tags', [])
        titulo = metadata.get('title')
        wiki_pages.append((file_name, titulo, tags))

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

    if membros[autor].get('github'):
        formatter = "https://avatars.githubusercontent.com/{}?size=250"
        username = membros[autor]['github']
    elif membros[autor].get('email'):
        formatter = "http://www.gravatar.com/avatar/{}?s=250"
        username = hashlib.md5(membros[autor]['email'].strip().lower().encode("utf-8")).hexdigest()
    elif membros[autor].get('twitter'):
        formatter = "http://avatars.io/twitter/{}"
        username = membros[autor]['twitter']
        username = username[1:] if username.startswith("@") else username

    return formatter.format(username)


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


if __name__ == '__main__':
    func_name = sys.argv[1]
    if func_name == 'tags_generator':
        tags_wiki_generator()
