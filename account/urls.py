from django.urls import include, path
from . import views
"""
Views including django.contrib.auth.urls -- >
https://docs.djangoproject.com/en/2.2/topics/auth/default/#using-the-views
"""
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name="register"),
    path('edit/', views.edit, name='edit'),
]