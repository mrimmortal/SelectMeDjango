from rest_framework import generics
from common.models import *
from photographer.Serializers import *
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

#--------------------------PastEvent Model API classes (List And CRUD)---------------------------------
class CreateEventListView(generics.ListCreateAPIView):
    queryset = sm_event.objects.all()
    serializer_class = PastEventSerializer
    
class RUD_Event(generics.RetrieveUpdateDestroyAPIView):
    queryset = sm_event.objects.all()
    serializer_class = PastEventSerializer
#--------------------------End PastEvent Model API classes (List And CRUD)------------------------------