from django.urls import path
from main import views

app_name = 'main'
urlpatterns = [
	# ex: /todos/
	path('', views.IndexView.as_view(), name='index'),
	# ex: /todos/addList
	path('addlist/', views.addList, name='add_list'),
	# ex: /todos/1/
	path('postman/', views.task_list),
	path('postman/<int:pk>/', views.task_list_detail),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	# ex: /todos/1/deleteList/
	path('<int:list_id>/deletelist/', views.deleteList, name='delete_list'),
	# ex: /todos/1/completed/
    path('<int:pk>/completed/', views.ResultsView.as_view(), name='completed'),
	# ex: /todos/1/addtask/
    path('<str:list_id>/addtask/', views.addTask, name='add_task'),
];