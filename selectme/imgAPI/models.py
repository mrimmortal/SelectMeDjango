from django.db import models


class post_image(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="selected_pic", blank=True)


# Create your models here.
