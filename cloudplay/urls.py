"""
A list of URL's provided to the user. The user can add URL of his/her choice
and import it in cloud/urls.py
"""

from django.conf.urls import url
from . import views

urlpatterns = [
	# /music/
    url(r'^$', views.index, name='index'),

    # /music/712/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name = 'detail'),
]