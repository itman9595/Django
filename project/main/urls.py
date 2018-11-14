from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.AdvertList.as_view()),
    path('<int:pk>/', views.AdvertDetail.as_view(), name='detail'),
    path('postman/', views.adverts_list),
    path('postman/<int:pk>/', views.adverts_detail),
    path('login/', views.login)
]