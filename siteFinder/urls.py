
from django.conf.urls import url, include
from django.contrib import admin

from finder import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^finder/', include('finder.urls', namespace='gallery')),
]
