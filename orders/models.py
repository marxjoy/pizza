from django.db import models
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
        return f"Order {self.id}"


    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items)


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    meal = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, 
                                decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return self.id


    def get_cost(self):
        return self.price * self.quantity
    

    
    
    
    