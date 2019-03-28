from __future__ import unicode_literals

from django.contrib import admin
from para.models import Client
from para.models import Network_object

admin.site.register(Client)
admin.site.register(Network_object)