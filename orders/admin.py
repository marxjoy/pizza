from django.contrib import admin

from .models import Meal, Cart, Topping, SubTopping

admin.site.register(Meal)
admin.site.register(Cart)
admin.site.register(Topping)
admin.site.register(SubTopping)

