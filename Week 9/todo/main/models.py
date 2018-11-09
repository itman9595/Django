import datetime

from django.db import models
from django.utils import timezone

class Task_List(models.Model):
	task_list_name = models.CharField(max_length=200)
	created_at = models.DateTimeField('date published')
	def __str__(self):
		return self.task_list_name
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.created_at <= now
	was_published_recently.admin_order_field = 'created_at'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

class TaskManager(models.Manager):
	def for_user(self, user):
		return self.filter(owner=user)

class Task(models.Model):
	list_name = models.ForeignKey(Task_List, on_delete=models.CASCADE)
	task_order = models.AutoField(primary_key=True)
	created_at = models.DateTimeField('date published')
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.created_at <= now
	due_on = models.DateTimeField('date published')
	ADMIN = 'ADM'
	GUEST = 'GST'
	ROLES = (
		(ADMIN, 'Admin'),
		(GUEST, 'Guest'),
	)
	owner = models.CharField(
		max_length=5,
		choices=ROLES,
		default=ADMIN,
	)
	mark = models.BooleanField(default=False)
	objects = TaskManager()

class Author(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField()

	def __str__(self):
		return self.email