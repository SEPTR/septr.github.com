#!/usr/bin/env python

# Meta.
AUTHOR       = "webmaster@septrmtb.org"
SITENAME     = "SEPTR"
SITEURL      = "http://www.septrmtb.org"
FEED_DOMAIN  = SITEURL
TIMEZONE     = "America/New_York"
THEME        = "themes/v0"
STATIC_PATHS = ["documents", "images"]

# Do not generate any feeds.
FEED_ALL_ATOM      = None
CATEGORY_FEED_ATOM = None

# Do not autoreload when Emacs drops a lock file.
IGNORE_FILES = ["^.#"]

# URL Settings.
ARCHIVES_SAVE_AS = "archives/index.html"
ARCHIVES_URL     = "archives/"
ARTICLE_SAVE_AS  = "{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"
ARTICLE_URL      = "{date:%Y}/{date:%m}/{date:%d}/{slug}/"
AUTHOR_SAVE_AS   = "author/{slug}/index.html"
AUTHOR_URL       = "author/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"
CATEGORY_URL     = "category/{slug}/"
PAGE_SAVE_AS     = "{slug}/index.html"
PAGE_URL         = "{slug}/"
TAG_SAVE_AS      = "tag/{slug}/index.html"
TAG_URL          = "tag/{slug}/"
