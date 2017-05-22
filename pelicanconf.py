#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Comite Organizador'
SITENAME = 'Stallman en Jujuy'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Argentina/Jujuy'

DEFAULT_LANG = 'es'
DEFAULT_CATEGORY = 'inicio'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
	('Inicio', '/category/inicio.html'),
	('Conferencía', '/category/conferencia.html'),
 	('F.A.Q.', '/category/faq.html'),
	('GNU', '/category/gnu.html'),
	('Software Libre', '/category/software-libre.html')
	 )

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
THEME = 'pelican-blueidea'
# Display the search form
DISPLAY_SEARCH_FORM = True
