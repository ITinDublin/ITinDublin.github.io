#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import hashlib
import functools
import os
import posixpath
import random


def GET_WIKI_PAGES():
    content = 'content/pages/wiki'
    wiki_pages = []
    for page in os.listdir(content):
        ler_arquivo = open(content+'/'+page, 'r')
        titulo = ler_arquivo.readline()
        extensao = page.split(".")[1]
        url = page.split(".")[0]
        if extensao == 'md':
            titulo = titulo.replace("Title:", " ").strip()
        ler_arquivo.close()
        wiki_pages.append((url, titulo))

    return wiki_pages


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