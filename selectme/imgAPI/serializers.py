from django.db.models import fields
from rest_framework import serializers
from .models import post_image
from imgAPI import models
from common.models import *

class post_image_serializer(serializers.ModelSerializer):
    class Meta:
        model = post_image
        fields = "__all__"

class event_serializer(serializers.ModelSerializer):
    class Meta:
        model = sm_event
        fields = "__all__"        

    # def get_date(self, instance):
    #     date = DateTime.datetime.now()
    #     return date.strftime("%m/%d/%Y")
