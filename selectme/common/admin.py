from django.contrib import admin
from .models import post_image, sm_event, sm_user

# Rster your models here.


class imageadmin(admin.ModelAdmin):
    list_display = ['id', 'title']

admin.site.register(post_image, imageadmin)
admin.site.register(sm_user)
admin.site.register(sm_event)


