from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext as _

from cart.cart import Cart
from .forms import OrderForm
from .models import OrderItem


@login_required
def order_create_view(request):
    order_form = OrderForm()
    cart = Cart(request)

    if len(cart) == 0:
        messages.warning(request, _('you can not proceed to checkout because your cart is Empty'))
        return redirect('product_list')

    if request.method == 'POST':
        order_form = OrderForm(request.POST, )


        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order=order_obj,
                    product=product,
                    quantity=item['quantity'],
                    price=product.price,
                )
            cart.clear()

            request.user.firstname = order_obj.firtname
            request.user.lastname = order_obj.lastname
            request.user.save()

            messages.success(request, _('your order has successfully placed '))

    return render(request, 'orders/order_create.html', {
        'form': order_form,
    })


