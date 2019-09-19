from django import forms
from .models import Topping

MEAL_QUANTITY_CHOICES =[(i, str(i)) for i in range(1, 10)]

class MealQuantityForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=MEAL_QUANTITY_CHOICES,
                                      coerce=int)

class MealAdditivesCheeseForm(forms.Form):
    add_cheese = forms.BooleanField(required=False,
                                    initial=False)