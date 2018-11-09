from django.contrib import admin

from .models import Task, Task_List

class TaskInline(admin.TabularInline):
	model = Task
	extra = 3

class TaskListAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['task_list_name']}),
		("Date Published", {'fields': ['created_at'], 'classes': ['collapse']}),
	]
	inlines = [TaskInline]
	list_display = ('task_list_name', 'created_at', 'was_published_recently')
	list_filter = ['created_at']
	search_fields = ['task_list_name']

admin.site.register(Task_List, TaskListAdmin)
