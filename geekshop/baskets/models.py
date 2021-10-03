import statistics

from django.db import models

from users.models import User
from products.models import Product

# class BasketQuerySet(models.QuerySet):
#
#     def delete(self):
#         for item in self:
#             item.product.quantity += item.quantity
#             item.product.save()
#         super(BasketQuerySet, self).delete()


class Basket(models.Model):
    # objects = BasketQuerySet.as_manager()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    created_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукты {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    @staticmethod
    def total_quantity(user):
        baskets = Basket.objects.filter(user=user)
        return sum(basket.quantity for basket in baskets)

    @staticmethod
    def total_sum(user):
        baskets = Basket.objects.filter(user=user)
        return sum(basket.sum() for basket in baskets)

    @staticmethod
    def get_item(pk):
        return Basket.objects.get(pk=pk)

    # def delete(self,*args,**kwargs):
    #     self.product.quantity += self.quantity
    #     self.save()
    #     super().delete(*args,**kwargs)
    #
    # def save(self,*args,**kwargs):
    #     if self.pk:
    #         self.product.quantity -= self.quantity - self.__class__.objects.get(pk=self.pk).quantity
    #     else:
    #       self.product.quantity -= self.quantity
    #     self.product.save()
    #     super(Basket, self).save(*args,**kwargs)
