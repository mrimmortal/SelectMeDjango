from rest_framework import serializers
from .models import post_image


class post_image_serializer(serializers.ModelSerializer):
    class Meta:
        model = post_image
        fields = "__all__"

    # def get_date(self, instance):
    #     date = DateTime.datetime.now()
    #     return date.strftime("%m/%d/%Y")
