from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from cart.forms import AddToCartProductForm
from .models import Product, Comment
from .forms import CommentForm


def test_messages(request):
    result = _('hello mamad')
    messages.success(request, 'welcome')
    messages.warning(request, 'watch your account')
    messages.error(request, 'error 207i')
    return render(request, 'products/test_message.html')


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(active=True)
    template_name = "products/product_list.html"
    context_object_name = "products"


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_to_cart_form'] = AddToCartProductForm()
        context["comment_form"] = CommentForm
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    # def get_success_url(self):
    #     return reverse("product_detail")
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)
        obj.product = product

        messages.success(self.request, _('Comment Successfully Created'))

        return super().form_valid(form)

    