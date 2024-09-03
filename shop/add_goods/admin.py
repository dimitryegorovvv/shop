from django.contrib import admin
from .models import Goods, Category, CartItem

# Register your models here.
admin.site.register(Goods)
admin.site.register(CartItem)
admin.site.register(Category)