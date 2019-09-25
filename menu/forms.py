from django import forms
from .models import PizzaTopping, SubTopping

MEAL_QUANTITY_CHOICES =[(i, str(i)) for i in range(1, 10)]
MEAL_SIZE_CHOICES = [('L', 'Large'), ('S', 'Small')]

class MealQuantityForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=MEAL_QUANTITY_CHOICES,
                                      coerce=int)

class MealSizeForm(forms.Form):
    size = forms.TypedChoiceField(choices=MEAL_SIZE_CHOICES)

class ExtraCheeseOnSubForm(forms.Form):
    extra_cheese = forms.BooleanField(required=False,
                                    initial=False,
                                    label="Extra cheese + 0.50$")

class PizzaToppingForm(forms.Form):
    pizza_topping = forms.ModelChoiceField(queryset=PizzaTopping.objects.all(),
                                     label="Topping:",
                                     to_field_name="name")

    def __str__(self):
        return

class SubToppingForm(forms.Form):
    sub_toppings = forms.ModelMultipleChoiceField(queryset=SubTopping.objects.all(),
                                              label="Toppings + 0.50$",
                                              to_field_name="name")

    def __str__(self):
        return