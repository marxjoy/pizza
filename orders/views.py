from django.shortcuts import render
from .models import Order, OrderItem
from cart.cart import Cart
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def order_create(request):
    cart = Cart(request)
    user = User.objects.get(username=request.user.username)
    order = Order.objects.create(user=user)
    for item in cart:
        OrderItem.objects.create(order=order, 
                                 meal=item['meal'],
                                 quantity=item['quantity'],
                                 price=item['price'],)
    order.save()
    cart.clear()
    return render(request,
                  'orders/order/created.html',
                  {'order': order})

@login_required
def order_status(request):
    user = User.objects.get(username=request.user.username)
    orders = Order.objects.filter(user=user)
    return render(request,
                  'orders/order/status.html',
                  {'orders': orders})