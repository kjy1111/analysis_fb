import os

CONFIG = {'pagename': ['jtbcnews', 'chosun'],
          'common': {'base_url': 'https://graph.facebook.com/v3.0', 'since': '2017-01-01', 'until': '2017-12-31', 'fetch': False,
                     'result_directory': '__results__/crawling',
                     'access_token': 'EAACEdEose0cBAJQGgeoB29vWzbZAF9jCZBLxZBXK07q2MTGSmRuTV6YMNN5pxBIiSXWvLeTrUWrFCbGZAevgckC95pqUhOAMm6dwm2Nx7MHqD2ZANUcBMGpZACsoVgI0eIYYwlrGS73v8ZALUjkcroIWadsjpz2ZBQ55nhKtJQ1ZC3gwIQT3x80sC8KPiC1wF18xlMv5nbvlN6QZDZD'}
          }

if not os.path.exists(CONFIG['common']['result_directory']):
    os.makedirs(CONFIG['common']['result_directory'])