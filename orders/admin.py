from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created', 'completed', 'get_total_cost' ]
    list_filter = ['completed',]
    list_editable = ['completed', ]
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)