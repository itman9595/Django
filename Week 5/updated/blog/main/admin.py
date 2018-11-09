from django.contrib import admin

from .models import Post, Comment

class PostInline(admin.TabularInline):
	model = Comment
	extra = 3

class PostAdmin(admin.ModelAdmin):
	fieldsets = [
		("Post Info", {'fields': ['post_author', 'post_title', 'post_content']}),
		("Date Published", {'fields': ['created_at'], 'classes': ['collapse']}),
	]
	inlines = [PostInline]
	list_display = ('post_author', 'post_title', 'post_content', 'created_at', 'was_published_recently')
	list_filter = ['created_at']

admin.site.register(Post, PostAdmin)