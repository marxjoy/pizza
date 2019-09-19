from django.db import models
from menu.models import Meal
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, 
                             related_name='orders', 
                             on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return 'Order {}'.format(self.id)
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal,
                             related_name='order_items',
                             on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, 
                                decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return '{}'.format(self.id)
    
    def get_cost(self):
        return self.price * self.quantity
    

class OrderItemAdditive(models.Model):
    meal = models.ForeignKey(OrderItem,
                             related_name='additive',
                            on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    
    
    