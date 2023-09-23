from django.db import models

from users.models import Customuser


class ProductCategory(models.Model):
    name = models.CharField('Название категории', max_length=130, unique=True)
    description = models.TextField('Описание категории', null=True, blank=True)

    class Meta:
        verbose_name = 'Категория продукта'
        verbose_name_plural = 'Категории продуктов'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('Название продукта', max_length=220)
    description = models.TextField('Описание товара')
    price = models.DecimalField('Цена товара', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField('Количества товара', default=0)
    image = models.ImageField('Фото', upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продкты'

    def __str__(self):
        return f'Продукт: {self.name} Категория: {self.category.name}'


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(to=Customuser, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user} Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price
