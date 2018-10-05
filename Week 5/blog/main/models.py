import datetime

from django.db import models
from django.utils import timezone

class Post(models.Model):
	post_author = models.CharField(max_length=200)
	post_title = models.CharField(max_length=100)
	post_content = models.CharField(max_length=500)
	created_at = models.DateTimeField('date published')
	def __str__(self):
		return self.post_title
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.created_at <= now
	was_published_recently.admin_order_field = 'created_at'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

class Comment(models.Model):
	post_author = models.ForeignKey(Post, on_delete=models.CASCADE)
	comment_author = models.CharField(max_length=200)
	comment_content = models.CharField(max_length=1000)
	created_at = models.DateTimeField('date published')
	def __str__(self):
		return self.comment_content
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.created_at <= now
	was_published_recently.admin_order_field = 'created_at'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'