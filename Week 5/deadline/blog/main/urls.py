from django.urls import path

from . import views
app_name = 'main'
urlpatterns = [
	
	# ex: /blog/
	path('', views.IndexView.as_view(), name='index'),
	# ex: /blog/1
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),

];