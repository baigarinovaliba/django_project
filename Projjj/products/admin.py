from django.contrib import admin
from .models import *
# Register your models here.

#Вкладка для того чтобы картинки добавлялись в окне продуктов
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


#Панель для добавления имен продуктов
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields ]
    inlines = [ProductImageInline]

    class Meta:
        model = Product

admin.site.register(Product,ProductAdmin)

#Панель для добавления картинок на продукты
class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage


admin.site.register(ProductImage, ProductImageAdmin)