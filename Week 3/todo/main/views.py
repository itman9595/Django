from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import datetime

from .models import Task_List, Task

class IndexView(generic.ListView):
	template_name = 'main/index.html'
	task_array = [
		{'due_on':  datetime.datetime(2018, 9, 21), 'owner': Task.ROLES[0][1], 'mark': True},
		{'due_on':  datetime.datetime(2018, 9, 23), 'owner': Task.ROLES[0][1], 'mark': False},
		{'due_on':  datetime.datetime(2018, 10, 11), 'owner': Task.ROLES[1][1], 'mark': True},
		{'due_on':  datetime.datetime(2018, 11, 5), 'owner': Task.ROLES[0][1], 'mark': True},
		{'due_on':  datetime.datetime(2018, 12, 3), 'owner': Task.ROLES[1][1], 'mark': False},
	]

	# Delete sqllite database in /todo folder before uncommenting it, apply migration, then comment again, in order to avoid problems

	# tl = Task_List(task_list_name="List 1", created_at=timezone.now())
	# tl.save()

	# for task in task_array:
	# 	tl.task_set.create(created_at=timezone.now(), due_on=task['due_on'], owner=task['owner'], mark=task['mark'])

	# print("Here: {}".format(tl.task_set.all()))
	# print(tl.id)
	# print(tl.task_list_name)
	print(Task_List.objects.get(pk=1).task_set.all())

	def get_queryset(self):
		"""
		Return the last ten published tasks (not including those set to be
		published in the future).
		"""        
		return Task_List.objects.filter(
			created_at__lte=timezone.now(),
		).order_by('-created_at')[:10]
	context_object_name = 'latest_task_list'

class DetailView(generic.DetailView):
	model = Task_List
	template_name = 'main/todo_list.html'

	def get_queryset(self):
		return Task_List.objects.filter(
			created_at__lte=timezone.now(),
		)

class ResultsView(generic.DetailView):
	model = Task_List
	template_name = 'main/completed_todo_list.html'
	def get_queryset(self):
		return Task_List.objects.filter(
			created_at__lte=timezone.now(),
		)