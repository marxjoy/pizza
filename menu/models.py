from django.db import models
from django.urls import reverse

class Topping(models.Model):
    pass 

class Category(models.Model):
    name = models.CharField(max_length=200, 
                            db_index=True)
    slug = models.SlugField(max_length=200, 
                            db_index=True, 
                            unique=True,
                           )
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('menu:meal_list_by_category', args=[self.slug])

 
    
class Meal(models.Model):
    SIZE = [('Small', 'small'), ('Large', 'large')]
    category = models.ForeignKey(Category, 
                                 related_name='meals', 
                                 on_delete=models.CASCADE,)
    name = models.CharField(max_length=200, 
                            db_index=True)
    slug = models.SlugField(max_length=200, 
                            db_index=True)
    price = models.DecimalField(max_digits=10, 
                                decimal_places=2)
    size = models.CharField(choices=SIZE,
                            max_length=20,
                            blank='True')
    pizza_toppings_quantity = models.IntegerField(blank='True', 
                                                  null='True')
    
    
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        
    def __str__(self):
        return '{} {}'.format(self.name, self.size)
    

