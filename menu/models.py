from django.db import models
from django.urls import reverse
import re


class Meal(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200, 
                            db_index=True,
                            )
    price_s = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                blank=True,
                                null=True,
                                verbose_name="price for Small meal")
    price_l = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                blank=True,
                                null=True,
                                verbose_name="price for Large meal")

    class Meta:
        index_together = (('id', 'slug'),)


    def __str__(self):
        return self.name


    def category(self):
        '''
        Gets category name based on Class Name
        :return:
        '''
        return re.sub(r'([a-z](?=[A-Z])|[A-Z](?=[A-Z][a-z]))',
                                  r'\1 ', self.__class__.__name__)


    def get_absolute_url(self):
        return reverse('menu:meal_detail', args=[self.id, self.slug])



class PizzaTopping(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)


    def __str__(self):
        return self.name



class SubTopping(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    def __str__(self):
        return self.name


class SicilianPizza(Meal):
    toppings_quantity = models.IntegerField(blank=True,
                                            null=True)

class RegularPizza(Meal):
    toppings_quantity = models.IntegerField(blank=True,
                                            null=True)

class Sub(Meal):
    toppings_are_available = models.BooleanField(blank=True)
    extra_cheese_available = models.BooleanField(blank=True,
                                       default=True)

class Pasta(Meal):
    pass


class Salad(Meal):
    pass


class DinnerPlatter(Meal):
    pass
