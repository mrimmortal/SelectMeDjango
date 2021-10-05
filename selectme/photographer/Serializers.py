from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from common.models import *
from common.serializers import *

                
class CustomerSerializer(serializers.ModelSerializer):      
    customer = UserSerializer()
    photographer_owner = UserSerializer()
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