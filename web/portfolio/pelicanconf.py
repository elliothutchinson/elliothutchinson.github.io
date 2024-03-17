AUTHOR = "Elliot"
SITENAME = "Elliot Hutchinson"
SITESUBTITLE = "Software Engineering"
SITEURL = "http://localhost:9000"

PORT = 9000
BIND = "0.0.0.0"

OUTPUT_PATH = "output/"
PATH = "content"
STATIC_PATHS = ["images", "static"]
EXTRA_PATH_METADATA = {
    "static/CNAME": {"path": "CNAME"},
    "static/favicon.png": {"path": "favicon.ico"},
    "static/robots.txt": {"path": "robots.txt"},
}

THEME = "theme/alkaline"
TIMEZONE = "US/Eastern"
DEFAULT_LANG = "en"
DEFAULT_PAGINATION = 5

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = "Articles"
INDEX_SAVE_AS = "blog/index.html"
ARTICLE_SAVE_AS = "blog/{slug}.html"
ARTICLE_URL = "blog/{slug}"
PAGE_URL = "pages/{slug}"
DRAFT_PAGE_URL = "drafts/pages/{slug}"
DRAFT_URL = "drafts/{slug}"
AUTHOR_URL = "author/{slug}"
CATEGORY_URL = "category/{slug}"
TAG_URL = "tag/{slug}"

ARCHIVES_URL = "archives"
AUTHORS_URL = "authors"
CATEGORIES_URL = "categories"
TAGS_URL = "tags"

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = (
#     ("Archives", "archives"),
#     ("Categories", "categories"),
#     ("Tags", "tags"),
#     ("Authors", "authors"),
)

LINKS = (
#     ("Pelican", "https://getpelican.com"),
#     ("Python", "https://www.python.org"),
#     ("Jinja2", "https://palletsprojects.com/p/jinja"),
)

# Alkaline theme settings
ALK_PROFILE_IMG_URL = "images/me.jpg"
ALK_FOOTER_TEXT = "© 2016 - 2024 Elliot Hutchinson"
ALK_DEBUG_URLS = False
ALK_DISPLAY_BLOG_LINK = True
ALK_BLOG_URL = "blog"
ALK_DRAFTS_URL = "drafts"
ALK_PAGES_URL = "pages"
ALK_GITHUB_URL = "https://github.com/elliothutchinson"
ALK_LINKEDIN_URL = "https://linkedin.com/in/elliothutchinson"
ALK_SOCIAL_IMG_URLS = (
    ("images/linkedin.svg", "https://linkedin.com/in/elliothutchinson"),
    ("images/github.svg", "https://github.com/elliothutchinson"),
)
