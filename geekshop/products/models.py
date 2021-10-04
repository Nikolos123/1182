from django.db import models


# Create your models here.

class ProductsCategory(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='products_images',blank=True)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductsCategory,on_delete=models.CASCADE)

    def __str__(self):
        return  f'{self.name} | {self.category}'

