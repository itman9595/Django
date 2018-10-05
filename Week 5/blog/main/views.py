from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import datetime

from .models import Post, Comment

class IndexView(generic.ListView):
	template_name = 'main/index.html'

	def get_queryset(self):
		"""
		Return the last ten published tasks (not including those set to be
		published in the future).
		"""       
		return Post.objects.filter(
			created_at__lte=timezone.now(),
		).order_by('-created_at')[:10]
	context_object_name = 'posts'

class DetailView(generic.DetailView):
	model = Post
	template_name = 'main/detail.html'

	def get_queryset(self):
		return Post.objects.filter(
			created_at__lte=timezone.now(),
		)