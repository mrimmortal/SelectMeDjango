from django.db import transaction
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import *
from common.models import *

class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = sm_user
        fields = '__all__'   

class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Token
        fields = ('key','user')

class sm_user_RegisterSerializer(serializers.ModelSerializer, RegisterSerializer):
    class Meta:
        model = sm_user
        fields = ['username','password1','password2','first_name','last_name','mobile','address']
            # Define transaction.atomic to rollback the save operation in case of error
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.first_name = self.data.get('first_name')
        user.last_name = self.data.get('last_name')
        user.mobile = self.data.get('mobile')
        user.address = self.data.get('address')
        user.save()
        return user
        
     

class EventSerializer(serializers.ModelSerializer):    
    class Meta:
        model = sm_event
        fields = '__all__'
        





    
    
