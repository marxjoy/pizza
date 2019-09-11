from django.shortcuts import render
from .models import Order, OrderItem
from cart.cart import Cart
from django.contrib.auth.models import User

def order_create(request):
    cart = Cart(request)
    user = User.objects.get(username=request.user.username)
    order = Order.objects.create(username=user.username,
                                 first_name=user.first_name,
                                 last_name=user.last_name,
                                 email=user.email,
                                )
    for item in cart:
        OrderItem.objects.create(order=order, 
                                   meal=item['meal'],
                                   price=item['quantity'])
    order.save()
    cart.clear()
    return render(request,
                  'orders/order/created.html',
                  {'order': order})

def order_status(request):
    user = User.objects.get(username=request.user.username)
    orders = Order.objects.filter(username=user.username)
    return render(request,
                  'orders/order/status.html',
                  {'orders': orders})