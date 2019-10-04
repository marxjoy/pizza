from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from .cart import Cart
from django.contrib.auth.decorators import login_required
from decimal import Decimal


@login_required
def cart_add(request):
    cart = Cart(request)
    meal_desc = request.POST['meal_name']
    quantity = request.POST['quantity']
    if 'size' in request.POST:
        if request.POST['size'] == 'L':
            price = Decimal(request.POST['price_l'])
            meal_desc += ' Large'
        else:
            price = Decimal(request.POST['price_s'])
            meal_desc += ' Small'
    else:
        try:
            price = Decimal(request.POST['price_s'])
        except:
            price = Decimal(request.POST['price_l'])

    if 'pizza_topping' in request.POST:
        meal_desc += ' Toppings: '
        topping = request.POST.getlist('pizza_topping')
        meal_desc += ', '.join(topping)

    if 'sub_toppings' in request.POST:
        meal_desc += ' Toppings: '
        topping = request.POST.getlist('sub_toppings')
        price += (Decimal(0.5 * len(topping)))
        meal_desc += ', '.join(topping)

    if 'extra_cheese' in request.POST:
        if request.POST['extra_cheese']:
            meal_desc += ' + Extra Cheese '
            price += Decimal(0.5)

    cart_item = CartItem.objects.create(meal_description=meal_desc, quantity=quantity,
                         price=price)
    cart_item.save()
    cart.add(cart_item.id)
    return redirect('cart:cart_detail')


@login_required
def cart_remove(request, meal_id):
    cart = Cart(request)
    meal = get_object_or_404(CartItem, id=meal_id)
    cart.remove(meal.id)
    return redirect('cart:cart_detail')


@login_required
def cart_detail(request):
    cart = Cart(request)
    return render(request, 
                  'cart/detail.html',
                  {'cart': cart})