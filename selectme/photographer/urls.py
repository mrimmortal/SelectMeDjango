from django.urls import path
from photographer.views import *

urlpatterns = [
    #-----------Past Event-------------
    path('past-event-list/',PastEventListView.as_view(), name='past-event-list'),   
    path('past-event/<int:pk>/',RUD_PastEvent.as_view(), name ='past-event')
    #-----------Past Event-------------
]