from django.contrib import admin
from .models import *

@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    # для автозаполнения slug'ов
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
@admin.register(UnderCategoryModel)
class UnderCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        verbose_name = 'Податегория'
        verbose_name_plural = 'Подкатегории'

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category_id', 'inorder')
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

@admin.register(RequestsModel)
class RequestsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'car_mark', 'acum')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'