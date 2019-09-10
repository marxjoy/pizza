from django.contrib import admin
from .models import Category, Meal

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug' ]
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ['name', 'size','category', 'price', 'pizza_toppings_quantity' ]
    list_filter = ['category', 'size']
    list_editable = ['price', ]
    prepopulated_fields = {'slug': ('name', 'size')}
