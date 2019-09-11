from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['meal']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name','email', 'created', 'completed' ]
    list_filter = ['completed',]
    list_editable = ['completed', ]
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)