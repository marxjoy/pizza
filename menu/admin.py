from django.contrib import admin
from .models import SicilianPizza, RegularPizza, DinnerPlatter, Salad, Sub, \
Pasta, PizzaTopping, SubTopping


@admin.register(SicilianPizza, RegularPizza, DinnerPlatter, Salad, Sub, Pasta)
class MealAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price_s', 'price_l']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(PizzaTopping, SubTopping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = ['name']