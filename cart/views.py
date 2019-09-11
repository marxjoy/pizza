from django.shortcuts import render, redirect, get_object_or_404
from menu.models import Meal
from .cart import Cart
from django.contrib.auth.decorators import login_required

@login_required
def cart_add(request, meal_id):
    cart = Cart(request)
    meal = get_object_or_404(Meal, id=meal_id)
    # tutaj dobór dodatków do pizzy lub subs
    cart.add(meal)
    return redirect('menu:meal_list')

@login_required
def cart_remove(request, meal_id):
    cart = Cart(request)
    meal = get_object_or_404(Meal, id=meal_id)
    cart.remove(meal)
    return redirect('cart:cart_detail')
    

@login_required
def cart_detail(request):
    cart = Cart(request)
    return render(request, 
                  'cart/detail.html',
                  {'cart': cart})