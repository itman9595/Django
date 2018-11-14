from django.db import models
from django.contrib.auth.models import User

class AdvertManager(models.Manager):
	def for_user(self, user):
		return self.filter(owner=user)

class Advert(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    number_of_views = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = AdvertManager()

