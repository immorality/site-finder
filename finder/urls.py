from django.conf.urls import url
from finder import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search),
    url(r'^list/$', views.matches, name='matches'),
]