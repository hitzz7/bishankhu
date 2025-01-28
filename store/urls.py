from . import views
from django.urls import path
app_name = 'store'

urlpatterns = [
    path('',views.home, name="home"),
    path('/product',views.product, name="product"),
    path('/service',views.service, name="service"),
    path('/about',views.about, name="about"),
    path('/contact',views.contact, name="contact"),
    path('/message',views.message, name="message"),
]
