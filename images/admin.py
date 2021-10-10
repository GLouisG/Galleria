from django.contrib import admin

from images.models import Category, Image, Location

# Register your models here.
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Image)