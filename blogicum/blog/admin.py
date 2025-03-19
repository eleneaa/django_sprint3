from django.contrib import admin

from .models import Post, Blog_Category, Location

admin.site.register(Post)
admin.site.register(Blog_Category)
admin.site.register(Location)

# Register your models here.
