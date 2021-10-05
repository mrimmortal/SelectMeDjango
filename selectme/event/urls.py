from event.views import CreateEventListView, RUD_Event
from django.urls import path
from photographer.views import *

urlpatterns = [
    #-----------Past Event-------------
    path('event-list/',CreateEventListView.as_view(), name='event-list'),   
    path('event/<int:pk>/',RUD_Event.as_view(), name ='event')
    #-----------Past Event-------------
]