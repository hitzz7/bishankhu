from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StoreStaticSitemap(Sitemap):
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        # return the URL name (from urls.py -> name="...")
        return ["store:home", "store:product", "store:service", "store:about", "store:contact"]

    def location(self, item):
        return reverse(item)
