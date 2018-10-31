"""Paraweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import web_app.views.index
import web_app.views.add_client
import web_app.views.client_details

urlpatterns = [
    url (r'^index$', web_app.views.index.page, name='index'),
    url(r'^$', web_app.views.index.page),
    url (r'^add_client$', web_app.views.add_client.page, name='add_client'),
    url(r'^$', web_app.views.add_client.page),
    url(r'^client_details-(?P<pk>\d+)$',web_app.views.client_details.page, name="client_details"),
]

urlpatterns += staticfiles_urlpatterns()