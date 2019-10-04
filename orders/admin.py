from django.contrib import admin
from .models import Order, OrderItem


class VillainInline(admin.StackedInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created', 'completed', 'get_total_cost']
    list_filter = ['completed', ]
    list_editable = ['completed', ]
    inlines = [VillainInline]