from decimal import Decimal
from django.conf import settings
from menu.models import Meal

class Cart:
    
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    def add(self, meal, quantity=1, update_quantity=False):
        meal_id = str(meal.id)
        if meal_id not in self.cart:
            self.cart[meal_id] = {'quantity': 0,
                                  'price': str(meal.price)}
        if update_quantity:
            self.cart[meal_id]['quantity'] = quantity
        else:
            self.cart[meal_id]['quantity'] += quantity
        self.save()
            
    def save(self):
        self.session.modified = True
        
    def remove(self, meal):
        meal_id = str(meal.id)
        if meal_id in self.cart:
            if self.cart[meal_id]['quantity'] == 1:
                del self.cart[meal_id]
            else:
                self.cart[meal_id]['quantity'] -= 1
            self.save()
            
    def __iter__(self):
        meal_ids = self.cart.keys()
        
        meals = Meal.objects.filter(id__in=meal_ids)
        
        cart = self.cart.copy()
        for meal in meals:
            cart[str(meal.id)]['meal'] = meal
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
        
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
        
    