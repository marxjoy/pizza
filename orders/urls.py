from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("cart", views.cart_view, name="cart"),
    path("meal_detail/<int:id>/", views.meal_detail, name="meal_detail"),
    path("add_meal/<int:id>/", views.add_meal, name="add_meal"),
    path("remove_meal/<int:id>/", views.remove_meal, name="remove_meal"),
    path("order", views.order, name="order"),
    path("confirm", views.confirm, name="confirm"),
]
