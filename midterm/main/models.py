import datetime

from django.db import models
from django.utils import timezone

class Person(models.Model):
	name = models.CharField(max_length=200)
	telephone = models.CharField(max_length = 200)
	city = models.CharField(max_length = 200)

class Restaurant(models.Model):
	name = models.CharField(max_length = 200)
	number = models.CharField(max_length = 200)
	telephone = models.CharField(max_length = 200)
	city = models.CharField(max_length = 200)
	user = models.ForeignKey(Person, on_delete=models.CASCADE)

class Dish(models.Model):
	name = models.CharField(max_length = 200)
	description = models.CharField(max_length = 200)
	price = models.CharField(max_length = 200)
	user = models.ForeignKey(Person, on_delete=models.CASCADE)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Review(models.Model):
	rating = models.CharField(max_length = 200)
	comment = models.CharField(max_length = 200)
	date = models.DateTimeField('date published')

class RestaurantReview(models.Model):
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	review = models.ForeignKey(Review, on_delete=models.CASCADE)
	user = models.ForeignKey(Person, on_delete=models.CASCADE)

class DishReview(models.Model):
	dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
	review = models.ForeignKey(Review, on_delete=models.CASCADE)
	user = models.ForeignKey(Person, on_delete=models.CASCADE)





