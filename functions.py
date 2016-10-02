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


def tag_wiki_path(tag_index, default_path='output/wiki/tags'):
    for tag, values in tag_index.items():
        path = os.path.join(copy(default_path), "/".join([tag, 'index.html']))
        try:
            os.makedirs(os.path.dirname(path))
        except FileExistsError:
            pass

        path_for_cp = [
            ('output/wiki.html', 'output/wiki/index.html'),
            ('output/tags-wiki.html', 'output/wiki/tags/index.html'),
            ('output/wiki.html', path)
        ]
        for file1, file2 in path_for_cp:
            shutil.copy2(file1, file2)

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
        with open(path, 'w', encoding='utf-8') as f:
            f.write(soup.prettify())

        logging.info('Writing %s', path)


def create_index_tags(tags, file_name, titulo, tag_index):
    for tag in tags:
        tag_index[str(tag)].append({'url': file_name, 'titulo': titulo})

    return tag_index


def reader_wiki_files():
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


def tags_generator(create=True):
    tag_index = defaultdict(list)
    for file_name, titulo, tags in reader_wiki_files():
        if tags:
            create_index_tags(tags, file_name, titulo, tag_index)
    if create:
        tag_wiki_path(tag_index)
        return

    return tag_index


def GET_WIKI_PAGES():
    return reader_wiki_files()


def GET_TAGS_WIKI():
    tag_index = tags_generator(False)
    all_tags = tag_index.keys()
    return all_tags


def GET_AVATAR(autor, membros):
    if autor in membros:
        if 'github' in membros[autor]:
            formatter = "https://avatars.githubusercontent.com/{}?size=250"
            username = membros[autor]['github']
        elif 'email' in membros[autor]:
            formatter = "http://www.gravatar.com/avatar/{}?s=250"
            username = hashlib.md5(membros[autor]['email'].strip().lower().encode("utf-8")).hexdigest()
        elif 'twitter' in membros[autor]:
            formatter = "http://avatars.io/twitter/{}"
            username = membros[autor]['twitter']
            if username.startswith("@"):
                username = username[1:]
        else:
            formatter = "/theme/img/{}"
            username = "default_avatar.png"
    else:
        formatter = "/theme/img/{}"
        username = "default_avatar.gif"
    return formatter.format(username)


def GET_ARTICLE_IMAGE(article, root):
    if hasattr(article, 'image'):
        img = article.image
        if img.startswith('/'):
            img = img[1:]
        return img

    if not root:
        return ""

    base = os.path.join('content', root)
    banners = map(functools.partial(os.path.join, root), os.walk(base).next()[2])
    random.seed(article.date)
    return random.choice(banners)


def GET_ARTICLE_AT_GITHUB(article, repo, branch):
    base = posixpath.relpath(article.source_path, os.getcwd())
    return posixpath.join(repo, 'tree/', branch, base)


def GET_LINK(link):
    if link.startswith('http://') or link.startswith('https://'):
        return link
    else:
        return '/' + link

if __name__ == '__main__':
    func_name = sys.argv[1]
    if func_name == 'tags_generator':
        tags_generator()
