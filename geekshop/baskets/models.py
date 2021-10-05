import statistics

from django.db import models

from users.models import User
from products.models import Product


# class BasketQuerySet(models.QuerySet):
#
#     def delete(self,*args,**kwargs):
#         for item in self:
#             item.product.quantity += item.quantity
#             item.product.save()
#         super(BasketQuerySet, self).delete(*args,**kwargs)



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


    # def delete(self,*args,**kwargs):
    #     self.product.quantity +=self.quantity
    #     self.save()
    #     super(Basket, self).delete(*args,**kwargs)
    #
    # def save(self,*args,**kwargs):
    #     if self.pk:
    #         self.product.quantity -= self.quantity - self.get_item(int(self.pk))
    #     else:
    #         self.product.quantity -= self.quantity
    #     self.product.save()
    #     super(Basket, self).save(*args,**kwargs)

    @staticmethod
    def get_item(pk):
        return Basket.objects.get(pk=pk).quantity