from django.db import models
from users.models import CustomUser
# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=30, verbose_name='категория')

    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

class Goods(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    def formatted_price(self):
        if self.price == self.price.to_integral_value():
            return int(self.price)
        else:
            price_str = f"{self.price:.2f}"
            if price_str[-1] == '0':
                price_str = price_str[:-1]
            return float(price_str)
    description = models.CharField(max_length=500, verbose_name='описание')
    image = models.ImageField(upload_to='photos', verbose_name='изображение')
    category = models.ManyToManyField(Category, verbose_name='категория')
    popularity = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    # objects = ProductManager()


class CartItem(models.Model):
    good = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='товар')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='пользователь')
    quantity = models.PositiveIntegerField(default=1, verbose_name='количество')

    def __str__(self):
            return (f'{self.good.title} | {self.user} | {self.quantity}')

    class Meta:
        verbose_name = 'товар в корзине'
        verbose_name_plural = 'товары в корзине'