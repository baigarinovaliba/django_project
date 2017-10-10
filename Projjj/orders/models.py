from django.db import models
from products.models import Product
from django.db.models.signals import post_save

# Create your models here.

class Status(models.Model):
    status_name = models.CharField(max_length=54, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Status: %s " % self.status_name


    class Meta:
        verbose_name= "Status of order"
        verbose_name_plural= "Statuses of order"


class Order(models.Model):
    customer_name = models.CharField(max_length=54, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=54, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Total amount
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)



    def __str__(self):
        return "Order %s %s" %(self.id,self.status.status_name)


    class Meta:
        verbose_name='Order'
        verbose_name_plural='Orders'

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)



class ProducInOrder(models.Model):
    order = models.ForeignKey(Order,max_length=254, blank=True, null=True, default=None)
    product = models.ForeignKey(Product,max_length=254, blank=True, null=True, default=None)
    nmb =models.IntegerField(default=1)
    price_per_item=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    total_price=models.DecimalField(max_digits=10,decimal_places=2,default=0)#price*number
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)



    class Meta:
        verbose_name='Product'
        verbose_name_plural='Products'

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = self.nmb * price_per_item
        super(ProducInOrder, self).save(*args, **kwargs)
        order = self.order
        all_products_in_order = ProducInOrder.objects.filter(order=order, is_active=True)
        order_total_price = 0
        for item in all_products_in_order:
            order_total_price += item.total_price

        self.order.total_price = order_total_price
        self.order.save(force_update=True)
