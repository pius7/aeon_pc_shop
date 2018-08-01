# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from parts.models import parts_url, part

admin.site.register(parts_url)
admin.site.register(part)