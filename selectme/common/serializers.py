from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from common.models import sm_user


class sm_user_RegisterSerializer(serializers.ModelSerializer, RegisterSerializer):
   class Meta:
        model = sm_user
        fields = ['username','password1','password2','first_name','last_name','mobile','address']

    # Define transaction.atomic to rollback the save operation in case of error
        @transaction.atomic
        def save(self, request):
            user = super().save(request)
            print("==============>",self.data.get('first_name'))
            user.first_name = self.data.get('first_name')
            user.last_name = self.data.get('last_name')
            user.mobile = self.data.get('mobile')
            user.address = self.data.get('address')
            user.save()
            return user
