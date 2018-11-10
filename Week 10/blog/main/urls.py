from django.urls import path

from main import views
app_name = 'main'
urlpatterns = [
	
	# ex: /blog/
	path('', views.IndexView.as_view(), name='index'),
	# ex: /post_add
	path('post_add/', views.post_add, name='post_add'),
	# ex: /blog/1
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	# ex: blog/1/comment_add
	path('<int:post_id>/comment_add/', views.comment_add, name='comment_add'),

];