from django.shortcuts import render, redirect, get_object_or_404
from .models import SicilianPizza, RegularPizza, DinnerPlatter, Salad, Sub, \
Pasta, PizzaTopping, SubTopping
from .forms import MealQuantityForm, ExtraCheeseOnSubForm, MealSizeForm, \
    PizzaToppingForm, SubToppingForm
import re


meal_categories = [SicilianPizza, RegularPizza, DinnerPlatter, Salad, \
                       Sub, Pasta]


def meal_list(request):
    meals_by_categories = {re.sub(r'([a-z](?=[A-Z])|[A-Z](?=[A-Z][a-z]))',
                                  r'\1 ', c.__name__)+'s':
                            c.objects.all() for c in meal_categories }
    return render(request,
                  'meal/list.html',
                  {'meals_by_categories': meals_by_categories,
                   'pizza_toppings': PizzaTopping.objects.all(),
                   'sub_toppings': SubTopping.objects.all(),
                  }
                 )


def meal_detail(request, meal_id, meal_slug):
    for meal_category in meal_categories:
        try:
            meal = get_object_or_404(meal_category, id=meal_id, slug=meal_slug)
        except:
            pass
    forms = [MealQuantityForm()]
    if meal.category() == "Sub":
        forms.append(ExtraCheeseOnSubForm)
    try:
        if meal.toppings_quantity:
            for i in range(meal.toppings_quantity):
                forms.append(PizzaToppingForm)
    except:
        pass
    try:
        if meal.toppings_are_available:
            forms.append(SubToppingForm())
    except:
        pass
    if meal.price_l and meal.price_s:
        forms.append(MealSizeForm())

    return render(request,
                  'meal/detail.html',
                 {'meal': meal,
                  'forms': forms,
                 })