from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^contact', views.contact, name = 'contact'),
    url(r'^your-name/', views.get_name, name = 'your-name'),
    url(r'^thanks', views.get_name),
]
