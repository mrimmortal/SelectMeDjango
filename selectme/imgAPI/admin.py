from django.contrib import admin
from .models import post_image

# Rster your models here.


class imageadmin(admin.ModelAdmin):
    list_display = ['id', 'title']

admin.site.register(post_image, imageadmin)


