AUTHOR = 'Tingyue Lai'
SITENAME = '悅來越好玩'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = 'zh-TW'

# Static paths
STATIC_PATHS = ['images', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Menu Items
MENUITEMS = (
    ('首頁', '/'),
    ('海外旅遊', '#', (
        ('日本', '/category/japan.html'),
        ('韓國', '/category/korea.html'),
        ('泰國', '/category/thailand.html'),
    )),
    ('玩樂地圖', '#', (
        ('台北', '/category/taipei.html'),
        ('台中', '/category/taichung.html'),
        ('高雄', '/category/kaohsiung.html'),
    )),
    ('精選住宿', '/category/accommodation.html'),
    ('美食特搜', '/category/food.html'),
    ('關於我', '/pages/about.html'),
)

# Page URL settings
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

# Google Analytics & Ads & Search Console
GOOGLE_ADSENSE = {
    'client': 'ca-pub-XXXXXXXXXXXXXXXX', # Replace with your AdSense Client ID
    'slot': 'XXXXXXXXXX' # Replace with your Ad Slot ID
}
GOOGLE_SEARCH_CONSOLE = 'VerificationCodeHere' # Replace with your GSC verification code
FAVICON = 'images/favicon.ico'

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Google Ads Settings
GOOGLE_ADSENSE = {
    'client': 'ca-pub-XXXXXXXXXXXXXXXX', # REPLACE THIS
    'slot': 'XXXXXXXXXX' # REPLACE THIS
}

# Theme Settings
THEME = 'theme/mytheme'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
