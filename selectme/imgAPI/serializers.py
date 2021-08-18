from django.db.models import fields
from rest_framework import serializers
from .models import post_image, sm_event
from imgAPI import models


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
