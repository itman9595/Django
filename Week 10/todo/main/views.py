from django.contrib.auth.models import User, Group
from django.views import generic
from rest_framework import viewsets
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from main.serializers import TaskListSerializer
from main.models import Task_List, Task, Author
from main.forms import TaskForm

app_name = 'main'

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

class DetailView(LoginRequiredMixin, generic.DetailView):
	model = Task_List
	template_name = 'main/todo_list.html'
	redirect_field_name = "/todos/"
	def get_queryset(self):
		return Task_List.objects.filter(
			created_at__lte=timezone.now(),
		)

class ResultsView(LoginRequiredMixin, generic.DetailView):
	model = Task_List
	template_name = 'main/completed_todo_list.html'
	redirect_field_name = "/todos/"
	def get_queryset(self):
		return Task_List.objects.filter(
			created_at__lte=timezone.now(),
		)

@csrf_exempt
def task_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        task_lists = Task_List.objects.all()
        serializer = TaskListSerializer(task_lists, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def task_list_detail(request, pk):
	"""
	Retrieve, update or delete a code snippet.
	"""
	try:
		task_list = Task_List.objects.get(pk=pk)
	except Task_List.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = TaskListSerializer(task_list)
		return JsonResponse(serializer.data)


	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = TaskListSerializer(task_list, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		task_list.delete()
	return HttpResponse(status=204)