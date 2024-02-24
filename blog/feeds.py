from django.contrib.syndication.views import Feed
from .models import Post

class LatestEntriesFeed(Feed):
    title = "blog latest posts"
    link = "/rss/feed"
    description = "best blog ever"

    def items(self):
        return Post.objects.filter(status=True)[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:80]
