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
LINKS = (('Free Software Foundation', 'https://my.fsf.org/civicrm/profile/create?gid=496&reset=1'),)
         
# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
	('Conferencía', '/category/conferencia.html'),
	('D.H.C.', '/category/dhc.html'),
	('Biografia', '/category/biografia.html'),
 	('Pre-Stallman', '/category/pre-stallman.html'),
	('Software Libre', '/category/software-libre.html'),
	('F.A.Q.', '/category/faq.html')
	 )

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
THEME = 'pelican-blueidea'
# Display the search form
DISPLAY_SEARCH_FORM = False
