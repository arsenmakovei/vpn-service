from django.urls import path

from vpn.views import SiteListView, SiteCreateView, proxy_site

urlpatterns = [
    path("", SiteListView.as_view(), name="site-list"),
    path("sites/create/", SiteCreateView.as_view(), name="site-create"),
    path(
        "statistics/",
        SiteListView.as_view(template_name="vpn/statistics_list.html"),
        name="statistics-list",
    ),
    path(
        "<str:user_site_name>/<int:site_id><path:routes_on_original_site>",
        proxy_site,
        name="proxy-site",
    ),
]

app_name = "vpn"
