from django.contrib.auth.models import AbstractUser
from django.db import models

class sm_user(AbstractUser):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=128)

# This table will provide meta data to the event mapping table
class sm_event(models.Model):
    customer = models.ForeignKey(sm_user,on_delete=models.CASCADE)
    photographer_owner = models.ForeignKey(sm_user,on_delete=models.CASCADE , related_name="photographer_owner")
    title = models.CharField(max_length=100)
    description  = models.CharField(max_length=1024)
    status = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    image_dir = models.CharField(max_length=255)
    is_share_with_customer = models.BooleanField(default=False) # is_share_with_customer photographer/customer can able to revoke the sharable link

# while sharing the event this mapper will identify who is the owner photographer and co owner photographer of the same event 
class event_mapping(models.Model):
    event = models.ForeignKey(sm_event,on_delete=models.CASCADE)
    user = models.ForeignKey(sm_user,on_delete=models.CASCADE)