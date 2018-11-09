from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import datetime

from .models import Task_List, Task

class IndexView(generic.ListView):
	template_name = 'main/index.html'

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