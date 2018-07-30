#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'vyos-users.jp'
SITENAME = u'vyos-users.jp'
SITEURL = ''

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = u'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['extra/CNAME', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

THEME = './themes/vyos-users-jp.github.io-theme'
BOOTSTRAP_NAVBAR_INVERSE = True
HIDE_SIDEBAR = True
CC_LICENSE = 'by-nc-sa'

DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [('Wiki', 'http://wiki.vyos-users.jp')]
