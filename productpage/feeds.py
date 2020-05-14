

from django.contrib.syndication.views import Feed
from .models import
from django.urls import reverse


class Archive(Feed):
    title = "Best Bids"
    link = "/archive/"
    description = "Updates on new complaints on Dreamrea entry."

    def items(self):
        return Comment.objects.all().order_by("-submit_date")[:5]

    def item_title(self, item):
        return item.user_name

    def item_description(self, item):
        return item.comment

    def item_link(self, item):
        return reverse('comment', kwargs={'object_pk': item.pk}