from django.shortcuts import render, get_object_or_404
from .models import Category, Meal

def meal_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    meals = Meal.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        meals = meals.filter(category=category)
    return render(request, 
                  'meal/list.html', 
                  {'category': category,
                   'categories': categories, 
                   'meals': meals,
                  }
                 )



