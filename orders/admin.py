from django.contrib import admin

from .models import Meal, Cart, Topping
# Register your models here.

admin.site.register(Meal)
admin.site.register(Cart)
admin.site.register(Topping)


