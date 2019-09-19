from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Meal, Topping
from .forms import MealQuantityForm, MealAdditivesCheeseForm

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

def meal_detail(request, meal_id, meal_slug):
    meal = get_object_or_404(Meal, id=meal_id, slug=meal_slug)
    
    forms = [MealQuantityForm()]
    if meal.category.name == 'Subs':
        forms.append(MealAdditivesCheeseForm())

    return render(request, 
                  'meal/detail.html',
                 {'meal': meal,
                  'forms': forms,
                 })


