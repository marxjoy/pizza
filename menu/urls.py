from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.meal_list, name='meal_list'),
    path('<slug:category_slug>/', views.meal_list, name='meal_list_by_category'),
    path('<int:meal_id>/<slug:meal_slug>/', views.meal_detail, name='meal_detail'),
]