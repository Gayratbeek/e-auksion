from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse

from .models import News


class RssFeed(Feed):
    title = 'News'


link = '/rss/'
description = 'Newsletter.'


def items(self):
    return News.objects.all()[:5]


#
# def item_title(self, item):
#     return item.title
#
#
# def item_description(self, item):
#     return item.desc

