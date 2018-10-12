from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import auth

from main.models import Post, Comment

def post_add(request):
	if(request.POST.get('addPostBtn')):
		p = Post(post_author=request.user, post_title=request.POST.get('post_title'), post_content = request.POST.get('post_content'), created_at=timezone.now())
		p.save()
		return redirect('/blog')

def comment_add(request, post_id):
	if(request.POST.get('addCommentBtn')):
		usr = request.user
		p = Comment(post_author=Post.objects.get(pk=post_id), comment_author = usr, comment_content=request.POST.get('post_content'), created_at=timezone.now())
		p.save()
		return redirect('/blog/'+str(post_id))

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