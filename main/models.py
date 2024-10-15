from django.db import models

class CategoryModel(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name='Название категории')
    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class ProductModel(models.Model):

    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(unique=True, max_length=100, verbose_name='Именная ссылка')

    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    full_price = models.FloatField(verbose_name='Полная цена')
    tradein_price = models.FloatField(verbose_name='Цена в трейд-ин')

    parameter1 = models.IntegerField(verbose_name='Ёмкость')
    parameter2 = models.IntegerField(verbose_name='Пусковой ток')
    parameter3 = models.CharField(verbose_name='Полярность', max_length=30)
    parameter4 = models.CharField(verbose_name='Габариты', max_length=30)
    parameter5 = models.CharField(verbose_name='Производство', max_length=30)
    parameter6 = models.IntegerField(verbose_name='Напряжение')
    parameter7 = models.CharField(verbose_name='Гарантия', max_length=30)
    parameter8 = models.CharField(verbose_name='Вес', max_length=30)

    inorder = models.BooleanField(verbose_name='В наличии', default=True)

    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT)
    under_category = models.ForeignKey('UnderCategoryModel', on_delete=models.PROTECT, blank=True, null=True)

    def get_absolute_url(self):
        return f'{self.category.name}/{self.slug}'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class UnderCategoryModel(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name='Название подкатегории', db_index=True)

    slug = models.SlugField(unique=True, max_length=100)
    cat = models.ForeignKey(CategoryModel, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

class RequestsModel(models.Model):
    name = models.CharField(
        max_length=40,
        verbose_name='Имя',
        blank=False
    )
    phone = models.CharField(
        max_length=12,
        verbose_name='Номер телефона',
        blank=False
    )
    car_mark = models.CharField(
        max_length=40,
        verbose_name='Марка авто',
        blank=False
    )
    problem = models.TextField(
        verbose_name='Текст заказчика',
        blank=True,
        null=True
    )

    acum = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Выбрано АКБ'
    )

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'