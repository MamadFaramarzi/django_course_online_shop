from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)

    firstname = models.CharField(_('firstname'), max_length=100)
    lastname = models.CharField(_('lastname'), max_length=100)
    phone_number = models.CharField(_('phone number'), max_length=15)
    address = models.CharField(_('address'), max_length=700)
    order_notes = models.CharField(_('order_notes'), max_length=500, blank=True)

    zarinpal_authority = models.CharField(max_length=255, blank=True)

    datetime_created = models.DateTimeField(_('date time of creation'), auto_now_add=True)
    datetime_modified = models.DateTimeField(_('date time of last edit'), auto_now=True)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_price(self):
        return sum(item.price * item.quantity for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='order')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='order_items', verbose_name='product')
    quantity = models.PositiveIntegerField(_('quantity'), default=1)
    price = models.PositiveIntegerField(_("$"))

    def __str__(self):
        return f'OrderItem {self.id} : {self.product} * {self.quantity} (price:{self.price})'
