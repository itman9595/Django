from django.contrib import admin

from .models import Person, Restaurant, Dish, Review, RestaurantReview, DishReview

class RestaurantInline(admin.TabularInline):
	model = Restaurant
	extra = 2

class DishInline(admin.TabularInline):
	model = Dish
	extra = 2

class RestaurantReviewInline(admin.TabularInline):
	model = RestaurantReview
	extra = 2

class DishReviewInline(admin.TabularInline):
	model = DishReview
	extra = 2

class PersonAdmin(admin.ModelAdmin):
	fieldsets = [
		("Person Info", {'fields': ['name', 'telephone', 'city']}),
	]
	inlines = [RestaurantInline]

admin.site.register(Person, PersonAdmin)

admin.site.register(Dish)

class ReviewAdmin(admin.ModelAdmin):
	fieldsets = [
		("Review Info", {'fields': ['rating', 'comment', 'date']}),
	]
	inlines = [RestaurantReviewInline, DishReviewInline]

admin.site.register(Review, ReviewAdmin)
