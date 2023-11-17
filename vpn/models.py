from urllib.parse import urlparse, unquote, quote

from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Site(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    url = models.URLField()
    page_views = models.PositiveIntegerField(default=0)
    data_sent_size = models.PositiveIntegerField(default=0)
    data_received_size = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def user_site_name(self) -> str:
        return slugify(self.name)

    @property
    def routes_on_original_site(self) -> str:
        site_url = urlparse(self.url)
        return f"{site_url.path}{site_url.query}" if site_url.query else site_url.path
