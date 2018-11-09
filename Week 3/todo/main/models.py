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
		max_length=2,
		choices=ROLES,
		default=ADMIN,
	)
	mark = models.BooleanField(default=False)