from django.contrib import admin

from homepage.models import Category, Recipe

admin.site.register(Category)
admin.site.register(Recipe)