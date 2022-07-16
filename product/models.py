from django.db import models


class Product(models.Model):
    product_id = models.PositiveIntegerField(primary_key=True)
    category_name = models.ForeignKey('ProductCategory', related_name='ProductCategory', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ("-product_id",)


class ProductCategory(models.Model):
    category_id = models.PositiveIntegerField(primary_key=True)
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"
        ordering = ("-category_id",)
