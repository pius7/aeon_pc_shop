# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from parts.models import parts_url



class Command(BaseCommand):
    def delete_item(self):
        
        par = parts_url.objects.all()
        for pa in par:
            pa.delete()
        
        
    def handle(self, *args, **options):
        self.delete_item()
