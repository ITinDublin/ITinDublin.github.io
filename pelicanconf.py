#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'itindublin'
SITENAME = 'It in Dublin'
THEME = 'themes/wiki'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'pt'

ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

CATEGORIES_URL = 'blog/categorias'
CATEGORIES_SAVE_AS = 'blog/categorias/index.html'
CATEGORY_URL = 'blog/categorias/{slug}'
CATEGORY_SAVE_AS = 'blog/categorias/{slug}/index.html'

TAG_URL = 'blog/tags/{slug}'
TAG_SAVE_AS = 'blog/tags/{slug}/index.html'
TAGS_URL = 'blog/tags'
TAGS_SAVE_AS = 'blog/tags/index.html'

AUTHOR_URL = 'blog/autores/{slug}'
AUTHOR_SAVE_AS = 'blog/autores/{slug}/index.html'
AUTHORS_URL = 'blog/autores'
AUTHORS_SAVE_AS = 'blog/autores/index.html'

INDEX_SAVE_AS = "index.html"

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
FEED_ALL_ATOM = None
FEED_ALL_RSS = None

# Navbar Links da Home Page
NAVBAR_HOME_LINKS = [
    {
        'title': 'Assuntos',
        'href': '#',
        'desc': 'Assuntos sobre TI na Irlanda',
        'children': [
            {
                'title': 'Review de empresas',
                'href': 'review-empresa',
            },
            {
                'title': 'Áreas de atuação',
                'href': 'area-atuacao',
            },
            {
                'title': 'Visto de trabalho',
                'href': 'visto-trabalho',
            },
        ]
    },
    {
        'title': 'Dúvidas',
        'href': '#',
        'desc': 'Dúvidas relacionadas a TI em Dublin',
        'children': [
            {
                'title': '--',
                'href': '#',
            },
            {
                'title': '--',
                'href': '#',
            },
        ]
    },
    {
        'title': 'Participe',
        'href': '#',
        'desc': 'Encontre e participe da comunidade e compartilhe suas dúvidas e idéias.',
        'children': [
            {
                'title': 'Lista de Discussões',
                'href': 'lista-de-discussoes',
            },
            {
                'title': 'Comunidades Locais',
                'href': 'comunidades-locais',
            },
            {
                'title': 'Eventos',
                'href': 'eventos',
            },
        ]
    },
    {
        'title': 'Contribua',
        'href': '#',
        'desc': 'Veja como contribuir e ajudar a comunidade crescer.',
        'children': [
            {
                'title': 'Contribuição',
                'href': 'contribua',
            },
        ]
    },
]

# Links sociais do rodapé
SOCIAL_LINKS = (
    {
        'href': 'https://github.com/ITinDublin',
        'icon': 'fa-github',
        'text': 'GitHub',
    },
    {
        'href': 'https://www.facebook.com/groups/ITinDublin/',
        'icon': 'fa-facebook-official',
        'text': 'Facebook',
    },
    {
        'href': 'https://groups.google.com/forum/#!forum/it-irlanda-br',
        'icon': 'fa-users',
        'text': 'Lista de Discussões',
    },
    {
        'href': 'http://itindublin.slack.com/messages/general',
        'icon': 'fa-slack',
        'text': 'Slack'
    }
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
