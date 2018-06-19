# FB API Wrapper Functions

from urllib.parse import urlencode
from .web_request import json_request

# ACCESS_TOKEN = 'EAACEdEose0cBABasNaQQGJJYIAcNGHMPm5hL8zfsh1T0ZAOfY0jZAx4WYs5Q1Sh1OlR956sD2qCIpxu4N5uIuvbmnHt3pnSuTcYvDFalWwMXNqH20jiTIFioRJDdBaM7tQLEZAZCZCB2eBh9vbSV6HSObwZAQQD9wY1chHddAyQDZAXzC07d9bZAsxxPlSIq5VbmXzpmDkBE9wZDZD'
# BASE_URL_FB_API = 'https://graph.facebook.com/v3.0'


def fb_gen_url(base_url, node='', **params):
    url = '%s/%s/?%s' % (base_url, node, urlencode(params))
    return url


def fb_name_to_id(pagename, base_url, access_token):
    url = fb_gen_url(base_url=base_url, node=pagename, access_token=access_token)
    json_result = json_request(url=url)
    return json_result.get('id')


def fb_fetch_posts(pagename, base_url, since, until, access_token):
    url = fb_gen_url(base_url=base_url, node=fb_name_to_id(pagename, base_url, access_token) + '/posts',
                     fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)',
                     since=since, until=until, limit=50, access_token=access_token)

    isnext = True

    while isnext is True:
        json_result = json_request(url=url)

        paging = None if json_result is None else json_result.get('paging')
        posts = None if json_result is None else json_result.get('data')

        url = None if paging is None else paging.get('next')
        isnext = url is not None

        yield posts