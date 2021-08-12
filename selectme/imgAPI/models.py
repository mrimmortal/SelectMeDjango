# from selectme.imgAPI.views import Image_Details
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import EmailField
from django.utils import timezone
import pathlib
import os
from datetime import datetime
from django.conf import settings


class post_image(models.Model):
    
    def make_path(instance, filename):
        initial_path = str(settings.MEDIA_ROOT)
        custom_path = str(instance.ImgDate.year) + "/" + \
            str(instance.ImgDate.month) + "/" + \
            str(instance.ImgDate.day) + "/" + instance.picture.name
        custom_path = os.path.join(initial_path, custom_path)
        print("custom_path===", custom_path)
        return str(custom_path)

    ImgDate = models.DateField()
    title = models.CharField(max_length=100)
    ImgDate = models.DateField()
    Userid = models.CharField(max_length=255, blank=True)
    Ceremony = models.CharField(max_length=255, blank=True)
    picture = models.ImageField(upload_to=make_path, blank=True)

# class sm_user(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     mobile = models.CharField(max_length=10)
#     address = models.CharField(max_length=128)

# # This table will provide meta data to the event mapping table
# class sm_event(models.Model):
#     customer = models.ForeignKey(sm_user)
#     photographer_owner = models.ForeignKey(sm_user)
#     title = models.CharField(max_length=100)
#     description  = models.CharField(max_length=1024)
#     status = models.CharField(max_length=50)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     image_dir = models.CharField(max_length=255)
#     is_share_with_customer = models.BooleanField(default=False) # is_share_with_customer photographer/customer can able to revoke the sharable link

# # while sharing the event this mapper will identify who is the owner photographer and co owner photographer of the same event 
# class event_mapping(models.Model):
#     event = models.ForeignKey(sm_event)
#     user = models.ForeignKey(sm_user)

    # def save(self, *args, **kwargs):
    #     initial_path = str(self.picture.path)
    #     custom_path = str(self.ImgDate.year) + '/' + \
    #         str(self.ImgDate.month) + '/' + \
    #         str(self.ImgDate.day) + '/' + str(self.picture.name)
    #     newpath = str(settings.MEDIA_ROOT + "/"+custom_path)
    #     print("newpath===", initial_path)
    #     os.rename(self.picture.path, newpath)
    #     # self.save()
    #     super().save(*args, **kwargs)


# initial_path = car.photo.path
# >> > car.photo.name = 'cars/chevy_ii.jpg'
# >> > new_path = settings.MEDIA_ROOT + car.photo.name
# >> >  # Move the file on the filesystem
# >> > os.rename(initial_path, new_path)
# >> > car.save()
# >> > car.photo.path
# '/media/cars/chevy_ii.jpg'
# >> > car.photo.path == new_path


# if os.path.exists(settings.MEDIA_ROOT+"/" + post_image.save()):
#     print("Folder exist")
# else:
#     print("Folder Created")
#     picture = models.ImageField(
#         upload_to=post_image.create, blank=True)


# if os.path.exists(settings.MEDIA_ROOT+"/" + post_image.create()):
#     {}
# else:
#     picture = models.ImageField(
#         upload_to=post_image.create, blank=True)
