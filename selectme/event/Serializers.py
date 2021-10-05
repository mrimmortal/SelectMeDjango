from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from common.models import *

class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = sm_event
        fields = ['customer',
                  'photographer_owner',
                  'title',
                  'description',
                  'event_address',
                  'status',
                  'start_date',
                  'end_date',
                  'is_share_with_customer']
