from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=254,blank=True, null=True, default=None)
    product_description = models.TextField(blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)


    def __str__(self):
        return "Product %s" % self.product_name

    class Meta:
        verbose_name='Product'
        verbose_name_plural='Products'


class ProductImage(models.Model):
    product = models.ForeignKey(Product,blank=True, null=True, default=None)
    product_image = models.ImageField(upload_to="product_images")
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)