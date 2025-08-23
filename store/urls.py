from . import views
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from store.sitemaps import StoreStaticSitemap


app_name = 'store'

sitemaps = {
    "store": StoreStaticSitemap,
}

urlpatterns = [
    path('',views.home, name="home"),
    path('Bishankhu-mustard-oil/',views.product, name="product"),
    path('mustard-oil-service/',views.service, name="service"),
    path('mustard-oil-about/',views.about, name="about"),
    path('bishankhu-mustard-oil-contact/',views.contact, name="contact"),
    path('message/',views.message, name="message"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]

