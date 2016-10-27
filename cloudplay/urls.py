"""
A list of URL's provided to the user. The user can add URL of his/her choice
and import it in cloud/urls.py
"""

from django.conf.urls import url
from . import views

app_name = 'cloudplay'

urlpatterns = [
	# /music/
    url(r'^$', views.index, name='index'),

    # /music/<album_id>/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name = 'detail'),

    # /music/<album_id>/favourite/
    url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name = 'favourite'),
]