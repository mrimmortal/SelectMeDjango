from django.urls import path
from photographer.views import *

urlpatterns = [
    #-----------Events-------------
    path('event-list/',EventListView.as_view(), name='event-list'),   
    path('event/<int:pk>/',RUD_Event.as_view(), name ='event'),
    #-----------Events-------------
    path('customer-list',CustomerList.as_view(), name ='customer-list')
]