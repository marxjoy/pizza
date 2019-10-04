from django.db import models


class CartItem(models.Model):
    meal_description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return '{}'.format(self.id)


    def get_cost(self):
        return self.price * self.quantity
