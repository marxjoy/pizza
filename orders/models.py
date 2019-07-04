from django.db import models
from django.contrib.auth.models import User

class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class OrderedTopping(models.Model):
    item = models.ForeignKey(Topping, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    
    def __str__s(self):
        return f"{self.item}"
    

class Meal(models.Model):
    SIZE = [
            ('L', 'Large'),
            ('S', 'Small')
           ]
    CATEGORY = [
                ('Regular', 'Regular Pizza'),
                ('Sicilian', 'Sicilian Pizza'),
                ('Salad', 'Salad'),
                ('Pasta', 'Pasta'),
                ('Subs', 'Subs'),
                ('Dinner', 'Dinner Platters')
               ]
    
    add_cheese_field = models.BooleanField(default=False, editable=False)
    id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    price_l = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Price of Large meal (if exist)') 
    name = models.CharField(max_length=64)
    toppings_quantity = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Quantity of toppings (if exist)')
    size = models.CharField(choices=SIZE, max_length=10, null=True, blank=True, editable=False)
    category = models.CharField(choices=CATEGORY, max_length=10)
      
    def __str__(self):
        return f"Meal: {self.name} Category: {self.category} Size: {self.size} ${self.price}"
   

class OrderedMeal(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Meal, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(OrderedTopping, blank=True, related_name='+')
    size = models.CharField(max_length=5)
    #add_cheese = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=5, decimal_places=2) 
        
    def __str__(self):
        i = ", ".join(str(seg.item.name) for seg in self.toppings.all())
        return f"{self.item.name} {self.item.price} Toppings: {i}"
    
    
    
    
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderedMeal)
    is_ordered = models.BooleanField(default=False)
      
    def __str__(self):
        i = ", ".join(str(seg) for seg in self.items.all())
    
        
        if self.is_ordered:
             return f"Order: {self.id} from {self.user}: {i}"
        else:
            return f"Uncompleted order"
        
        
            
       
    def count_items(self):
        i=0
        for item in self.items.all():
           i +=1
        return i
    
    def total_price(self):
        total_price=0
        for item in self.items.all():
            total_price += item.price
        return total_price
    
    
class SubTopping(models.Model):
    name = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.name}"