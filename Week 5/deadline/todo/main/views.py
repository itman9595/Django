from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import datetime

from .models import Task_List, Task

def addList(request):
	if(request.POST.get('addListBtn')):
		l = Task_List(task_list_name=request.POST.get('addListText'), created_at=timezone.now())
		l.save()
	return redirect('/todos')

def addTask(request, list_id):
	if(request.POST.get('addTaskBtn')):
		owner = "ADM"
		if(request.POST.get('owner')):
			owner = "GST"
		mark = "False"
		if(request.POST.get('mark_checkbox')=="on"):
			mark="True"
		t = Task(list_name=Task_List.objects.get(pk=list_id), created_at=timezone.now(), due_on=request.POST.get('due_on_datetime-local'),
			owner=owner, mark=mark)
		t.save()
	return redirect('/todos/'+str(list_id)+"/")

def deleteList(request, list_id):
	if(request.POST.get('deleteListBtn')):
		print("GG")
		Task_List.objects.get(pk=list_id).delete()
	return redirect('/todos/')		
	
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