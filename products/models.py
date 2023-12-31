from django.db import models
from django.shortcuts import reverse
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField


class Product(models.Model):
    title = models.CharField(verbose_name=_('product title'), max_length=100)
    description = RichTextField(verbose_name=_("product description"))
    short_description = models.TextField(_('short description'), blank=True)
    price = models.PositiveIntegerField(_("price"), default=0)
    active = models.BooleanField(verbose_name=_('product active'), default=True)
    image = models.ImageField(_('product image'), upload_to='product/product_cover/', blank=True, )

    datetime_created = models.DateTimeField(_('date time of creation'), default=timezone.now)
    datetime_modified = models.DateTimeField(_('date time of last edit'), auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])


class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    PRODUCT_CHOICES = [
        ('1', _('Very Bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('1', _('Good')),
        ('1', _('Perfect')),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments", verbose_name=_("product"))
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                               related_name="comments", verbose_name=_("Comment Author"))
    body = models.TextField(verbose_name=_("Comment Text"))
    stars = models.CharField(max_length=10, choices=PRODUCT_CHOICES, verbose_name=_('Your Score'))

    datetime_created = models.DateTimeField(_('date time of comment creation'), auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    active = models.BooleanField(_("valid"), default=True)

    # manager
    objects = models.Manager()
    active_comments_manager = ActiveCommentsManager()

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])
