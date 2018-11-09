from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.views import generic
from django.utils import timezone

import datetime

from main.models import Person

class IndexView(generic.ListView):
	template_name = 'main/index.html'

	def get_queryset(self):
		return Person.objects.filter(
			)
	context_object_name = 'persons'
