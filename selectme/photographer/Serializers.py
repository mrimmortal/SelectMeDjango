from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from common.models import *


class PastEventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = sm_event
        fields = '__all__'
