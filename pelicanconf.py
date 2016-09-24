#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'itindublin'
SITENAME = 'It in Dublin'
THEME = 'themes/wiki'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None

ARTICLE_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
TAGS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''

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
                'href': 'contribuicao',
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
