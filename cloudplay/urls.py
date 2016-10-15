"""
A list of URL's provided to the user. The user can add URL of his/her choice
and import it in cloud/urls.py
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name=''),
]