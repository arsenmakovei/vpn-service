from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from vpn.forms import SiteForm
from vpn.models import Site


class SiteListView(LoginRequiredMixin, ListView):
    model = Site

    def get_queryset(self):
        user = self.request.user
        queryset = Site.objects.filter(user=user)
        return queryset


class SiteCreateView(LoginRequiredMixin, CreateView):
    model = Site
    form_class = SiteForm
    success_url = reverse_lazy("vpn:site-list")

    def form_valid(self, form: SiteForm):
        form.instance.user = self.request.user
        return super().form_valid(form)


@login_required
def proxy_site(
    request, user_site_name: str, site_id: int, routes_on_original_site: str
):
    site = get_object_or_404(Site, id=site_id)
    parsed_site_url = urlparse(site.url)
    site_url = (
        f"{parsed_site_url.scheme}://{parsed_site_url.netloc}{routes_on_original_site}"
    )
    response = requests.get(site_url)
    soup = BeautifulSoup(response.content, "html.parser")

    updated_soup = update_links(soup, user_site_name, site_id, parsed_site_url)
    updated_response = HttpResponse(str(updated_soup))

    request_size = len(str(request.META)) + (len(request.body) if request.body else 0)
    response_size = len(updated_response.content)

    update_site_statistics(site, request_size, response_size)

    return updated_response


def update_links(
    soup: BeautifulSoup, user_site_name: str, site_id: int, parsed_site_url
):
    for link in soup.find_all("a", href=True):
        href = urlparse(link["href"])

        if href.path.startswith("/") and (
            not href.netloc or href.netloc == parsed_site_url.netloc
        ):
            routes_on_original_site = (
                f"{href.path}?{href.query}" if href.query else href.path
            )
            link["href"] = reverse_lazy(
                "vpn:proxy-site",
                kwargs=dict(
                    user_site_name=user_site_name,
                    site_id=site_id,
                    routes_on_original_site=routes_on_original_site,
                ),
            )

    return soup


def update_site_statistics(site: Site, request_size: int, response_size: int):
    site.page_views += 1
    site.data_sent_size += request_size
    site.data_received_size += response_size
    site.save()
