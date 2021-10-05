from rest_framework import generics
from common.models import *
from common.serializers import *
from photographer.Serializers import *
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


#--------------------------PastEvent API classes (List And CRUD)---------------------------------
class EventListView(generics.ListCreateAPIView):
    queryset = sm_event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id','status','photographer_owner')
    
class RUD_Event(generics.RetrieveUpdateDestroyAPIView):
    queryset = sm_event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id','status')
#--------------------------End PastEvent API classes (List And CRUD)------------------------------

#--------------------------Photographers Customer list  API classes (List And CRUD)---------------------------------
class CustomerList(generics.ListAPIView):
    queryset = sm_event.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id','photographer_owner')
#--------------------------End Photographers Customer list  API classes (List And CRUD)---------------------------------