from django.contrib import admin
from .models import *
# Register your models here.

class ProductInOrderAdmin(admin.TabularInline):
    model = ProducInOrder
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields ]
    inlines = [ProductInOrderAdmin]

    class Meta:
        model = Order
admin.site.register(Order,OrderAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)

class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProducInOrder._meta.fields]

    class Meta:
        model = ProducInOrder

admin.site.register(ProducInOrder, ProductInOrderAdmin)
