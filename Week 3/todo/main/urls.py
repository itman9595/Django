from django.urls import path

from . import views
app_name = 'main'
urlpatterns = [
	
	# ex: /todos/
	path('', views.IndexView.as_view(), name='index'),
	# ex: /todos/1/
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),


];