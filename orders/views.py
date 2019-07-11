from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Meal, Cart, Topping, OrderedMeal, OrderedTopping, SubTopping


def get_or_create_cart(request):
    """ Get User Cart or create new Cart for User
    """
    try:
        cart = Cart.objects.get(user=request.user, is_ordered=False)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user)
        cart.save()
    return cart

def index(request):
    """ Rendering Meal Menu View / Home Page
    """
    context = {
        "Toppings": Topping.objects.all(),
        "Categories": Meal.CATEGORY,
        "Meals": Meal.objects.order_by('category'),    
    }
    return render(request, "menu/index.html", context)

# Create your views here.

@login_required(login_url='login')
def add_meal(request, id):
    """ Add Meal from menu to User's Cart
    """
    cart = get_or_create_cart(request)
    meal = Meal.objects.get(id=id)
    
    if meal.price_l is None:
        price = meal.price
    else:
        price = meal.price
        price = request.POST['size']
    if price == str(meal.price_l):
        size = "Large"
    elif price == str(meal.price):
        size = "Small"
    else:
        size = "Large"
            
    sub_toppings = SubTopping.objects.all()
    name = meal.name
    # precyzowanie ordered_meal
    ordered_meal = OrderedMeal.objects.create(item=meal, name=name, price=price, size=size)
    if meal.category == 'Subs':
        if "cheese" in request.POST:
            ordered_meal.add_cheese = True
            ordered_meal.price = float(ordered_meal.price) + 0.5
            ordered_meal.name += '+ cheese 0.50$'
            
        if ordered_meal.name == "Steak + Cheese":
            for topping in sub_toppings:
                if request.POST['sub_topping']:
                    if str(topping) in request.POST['sub_topping']:
                        ordered_meal.sub_toppings.add(topping)
                        ordered_meal.price = float(ordered_meal.price) + 0.5
                        ordered_meal.name += '+ ' + str(topping) + '0.50$'
                        print(ordered_meal)
                        print('yeah')
            
    if meal.category == 'Sicilian' or meal.category == 'Regular':   
        toppings = []
        for i in range(meal.toppings_quantity):
            topping = request.POST["topping"+str(i)]
            toppings.append(topping)
        
        for topping in toppings:
            active_topping = Topping.objects.get(name=topping)
            ordered_topping = OrderedTopping.objects.create(item=active_topping)
            ordered_topping.save()
            ordered_meal.toppings.add(ordered_topping)
    
    ordered_meal.save()
    cart.items.add(ordered_meal)
    cart.save()  
    return redirect(cart_view)


@login_required(login_url='login')
def meal_detail(request, id):
    """ Modify meal (size, toppings, sub toppings)
    """
    meal = Meal.objects.get(id=id)
    if meal.category == 'Subs':
        add_cheese_field = True
    else:
        add_cheese_field = False
    if meal.price_l is None:
        is_sizable = False
    else:
        is_sizable = True
    if meal.name == "Steak + Cheese":
        is_steak_and_cheese_sub = True
    else:
        is_steak_and_cheese_sub = False
    if meal.category == 'Sicilian' or meal.category == 'Regular':
        toppings_quantity = meal.toppings_quantity
        topping_list = Topping.objects.all()
    else:
        toppings_quantity = 0
        topping_list = None
    if toppings_quantity is None:
        toppings_quantity = 0

    context = {
        "toppings_quantity": range(toppings_quantity),
        "meal": meal,
        "topping_list": topping_list,
        "add_cheese_field": add_cheese_field,
        "is_sizable": is_sizable,
        "is_steak_and_cheese_sub": is_steak_and_cheese_sub,
        "sub_toppings": SubTopping.objects.all(),
        
    }
    return render(request, "menu/detail.html", context)


@login_required(login_url='login')
def remove_meal(request, id):
    """ Remove meal from User's Cart
    """
    cart = Cart.objects.get(user=request.user, is_ordered=False)
    item = cart.items.get(id=id).delete()
    cart.save()
    return redirect(cart_view)


@login_required(login_url='login')
def cart_view(request):
    """ Cart View
    """
    cart = get_or_create_cart(request)
    items = cart.items.all()
    context = {
        'Cart': items,
        'total_price': cart.total_price(),
    }
    return render(request, "users/cart.html", context, )


@login_required(login_url='login')
def confirm(request):
    cart = Cart.objects.get(user=request.user, is_ordered=False)
    items = cart.items.all()
    context = {
         "message": "Confirm your order" ,
         "Cart": items,
         'total_price': cart.total_price(),
         'user': request.user,
        
    }
    return render(request, "users/compled.html", context,)


@login_required(login_url='login')
def order(request):
    """ Confirm order
    """
    cart = Cart.objects.get(user=request.user, is_ordered=False)
    cart.is_ordered=True
    cart.save()
    context = {
         "message": "Order compled" , 
    }
    return render(request, "users/cart.html", context,)