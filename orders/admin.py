from django.contrib import admin
from .models import Order, OrderItem

from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ['order', 'product', "quantity", "price"]
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'firstname', 'lastname', 'datetime_created', 'is_paid']
    inlines = [
        OrderItemInline
    ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']
