from . import views
from django.urls import path
app_name = 'store'

urlpatterns = [
    path('',views.home, name="home"),
    path('/Bishankhu-mustard-oil',views.product, name="product"),
    path('/mustard-oil-service',views.service, name="service"),
    path('/mustard-oil-about',views.about, name="about"),
    path('/bishankhu-mustard-oil-contact',views.contact, name="contact"),
    path('/message',views.message, name="message"),
]
