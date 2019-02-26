from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
	title=models.CharField(max_length=100)
	content=models.CharField(max_length=1000)
	image=models.ImageField(upload_to='profile_image', blank=True, null=True)


# Create your models here.
