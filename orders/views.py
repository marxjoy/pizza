from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Meal, Cart, Topping, OrderedMeal, OrderedTopping, SubTopping


def get_or_create_cart(request):
    try:
        cart = Cart.objects.get(user=request.user, is_ordered=False)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user)
        cart.save()
    return cart

def items_counter(request):
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user, is_ordered=False)
            items_counter = cart.count_items()
        except Cart.DoesNotExist:
            items_counter = 0    
    else:
        items_counter = 0
    return items_counter

# Create your views here.
def index(request):
    context = {
        "Toppings": Topping.objects.all(),
        "Categories": Meal.CATEGORY,
        "Meals": Meal.objects.order_by('category'),    
        "items_counter": items_counter(request),
    }
    return render(request, "menu/index.html", context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {"message": "Invalid"})
    else:
        return render(request, "users/login.html", {"items_counter": items_counter(request)})

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {"message": "Logged out"})

def register_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        if len(username) > 4 and len(password) > 4 and username.isalpha():
            user = User.objects.create_user(username, email, password)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            message = "User " + username + " created."
            return render(request, "users/login.html", {"message": message })
        else:
            message="Invalid"
            return render(request, "users/register.html", {"message": message })
    else:
        return render(request, "users/register.html", {"items_counter": items_counter(request)})

@login_required(login_url='login')
def add_meal(request, id):
    # tu dodaje do koszyka pizze id
    # wczytaj koszyk lub stworz nowy
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
        
    if meal.name == "Steak + Cheese":
        subtoppings = SubTopping.objects.all()
        pass
    
    # precyzowanie ordered_meal
    ordered_meal = OrderedMeal.objects.create(item=meal, price=price, size=size)
    print('ok')
    if meal.category == 'Subs':
        print('typ to', type(request.POST["cheese"]))
        ordered_meal.add_cheese = request.POST["cheese"]
    
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

    # precyzowanie ordered meal
    context = {
        "toppings_quantity": range(toppings_quantity),
        "meal": meal,
        "topping_list": topping_list,
        "items_counter": items_counter(request),
        "add_cheese_field": add_cheese_field,
        "is_sizable": is_sizable,
        "is_steak_and_cheese_sub": is_steak_and_cheese_sub,
        "sub_toppings": SubTopping.objects.all(),
        
    }
    return render(request, "menu/detail.html", context)


@login_required(login_url='login')
def remove_meal(request, id):
    cart = Cart.objects.get(user=request.user, is_ordered=False)
    item = cart.items.get(id=id).delete()
    cart.save()
    return redirect(cart_view)


@login_required(login_url='login')
def cart_view(request):
    # wczytaj koszyk lub stworz nowy
    cart = get_or_create_cart(request)
    items = cart.items.all()
    context = {
        'Cart': items,
         "items_counter": items_counter(request),
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
         "items_counter": items_counter(request),
        
    }
    return render(request, "users/compled.html", context,)



@login_required(login_url='login')
def order(request):
    cart = Cart.objects.get(user=request.user, is_ordered=False)
    cart.is_ordered=True
    cart.save()
    context = {
         "message": "Order compled" , 
         "items_counter": items_counter(request),
    }
    return render(request, "users/cart.html", context,)
