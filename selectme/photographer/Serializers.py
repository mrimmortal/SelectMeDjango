from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from common.models import *

class EventSerializer(serializers.ModelSerializer):    
    class Meta:
        model = sm_event
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = sm_user
        fields = '__all__'
                
class CustomerSerializer(serializers.ModelSerializer):  
    photographer_owner = UserSerializer(many=True, read_only=True) 
    customer = UserSerializer(many=True, read_only=True)
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
