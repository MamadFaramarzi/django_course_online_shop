from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin

from .models import Product, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['author', 'stars', "body", "active"]
    extra = 1


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ["title", "price", "active", "datetime_created",]
    inlines = [
        CommentInline,
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["product", 'author', 'stars', "body", "active", "datetime_created"]

