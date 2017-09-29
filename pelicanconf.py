#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ashley Arthur'
SITENAME = u'Ashley Arthur'
SITEURL = 'http://ashleyarthur.co.uk'
PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'
RELATIVE_URLS = True

DEFAULT_PAGINATION = 10
DEFAULT_CATEGORY = "Tech"
OUTPUT_PATH = 'docs/'
OUTPUT_SOURCES = True
OUTPUT_SOURCES_EXTENSION = ".md"
STATIC_PATHS = ['extra/CNAME']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


ARCHIVES_SAVE_AS = 'archives.html'

# Social widget
SOCIAL = (
	("Linkedin","https://uk.linkedin.com/in/ashley-arthur-4a918635"),
	('Github',"https://github.com/ash30"),
	('Flickr',"https://www.flickr.com/photos/ash30"),
)

# Style

# THEME = "/Users/ashleyarthur/Workspace/PROJECTS/pelican-themes_fork/pure"

PYGMENTS_STYLE = 'xcode'

SITELOGO = SITEURL + '/images/portrait.jpg'
FAVICON = SITEURL + '/images/favicon.ico'
ROBOTS = 'index, follow'
COPYRIGHT_YEAR = 2017
MAIN_MENU = True 
MENUITEMS = (
	('Archives', 'archives.html'),
        # ('Tags', 'tags.html'),
)
