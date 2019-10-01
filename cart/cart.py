from decimal import Decimal
from django.conf import settings
from .models import CartItem

class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get(settings.CART_SESSION_ID, {})
        self.session[settings.CART_SESSION_ID] = self.cart
    
    def add(self, cart_item_id):
        """
        Adds meal to Cart
        """
        item = CartItem.objects.get(id=cart_item_id)
        self.cart[cart_item_id] = {'id': item.id,
                                'meal': item.meal_description,
                                'price': str(item.price),
                                'quantity': item.quantity }
        self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        meal_ids = self.cart.keys()
        meals = CartItem.objects.filter(id__in=meal_ids)
        cart = self.cart.copy()
        for meal in meals:
            cart[str(meal.id)]['meal_id'] = meal
        for item in cart.values():
            item['meal'] = item['meal']
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def remove(self, cart_item_id):
        cart_item_id = str(cart_item_id)
        if cart_item_id in self.cart:
            del self.cart[cart_item_id]
            self.save()

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()