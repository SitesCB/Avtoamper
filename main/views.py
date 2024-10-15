from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpRequest
from django.views.generic import *
from .models import *
from itertools import chain
from urllib.request import *
from urllib.parse import *

class HomeView(ListView):
    template_name = 'main/index.html'
    model = ProductModel
    context_object_name = 'products'

    def get_queryset(self):
        return ProductModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['products'] = ProductModel.objects.all()
        context['categories'] = CategoryModel.objects.all()
        return context

class AboutView(TemplateView):
    template_name = 'main/about.html'

class DeliveryView(TemplateView):
    template_name = 'main/delivery.html'

class TradeinView(TemplateView):
    template_name = 'main/trade-in.html'

class WarrantyView(TemplateView):
    template_name = 'main/warranty.html'

class PrivacyView(TemplateView):
    template_name = 'main/privacy.html'

class DetailsView(TemplateView):
    template_name = 'main/details.html'

class CategoryView(ListView):
    template_name = 'main/category-list.html'
    model = ProductModel
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        need_slug = str(self.request.path).replace('/', '')
        need_category = get_object_or_404(CategoryModel, slug=need_slug)
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['products'] = ProductModel.objects.filter(category=need_category)
        context['categories'] = CategoryModel.objects.all()
        context['category_upper'] = {
            'choose_category' : need_category,
            'under_categories' : UnderCategoryModel.objects.filter(cat=need_category)
        }
        return context

class UnderCategoryView(ListView):
    template_name = 'main/under-category-list.html'
    model = ProductModel
    context_object_name = 'products'

    def get_context_data(self, **kwargs):

        context = super(UnderCategoryView, self).get_context_data(**kwargs)
        ''' получить список товаров под данной подкатегорией products '''
        ''' получить наименование подкатегории '''
        under_category = get_object_or_404(UnderCategoryModel, slug=str(self.request.path).split('/')[-2])
        current_category = str(self.request.path).split('/')[1]
        print(current_category, 'cur-cat')
        print(str(self.request.path).split('/')[-2])
        context['products'] = ProductModel.objects.filter(under_category=under_category.id)
        context['under_category'] = under_category
        context['cur_cat'] = current_category
        context['categories'] = CategoryModel.objects.all()
        return context

class ProductView(DetailsView):
    template_name = 'main/item.html'

    def get_context_data(self, **kwargs):
        need_slug = str(self.request.path).split('/')[-1]
        print(need_slug)
        product_item = get_object_or_404(ProductModel, slug=need_slug)
        context = super(ProductView, self).get_context_data(**kwargs)
        context['product_item'] = product_item
        context['products'] = self.find_similar_items(product_item)
        context['categories'] = CategoryModel.objects.all()

        return context

    def find_similar_items(self, item):
        items1 = ProductModel.objects.filter(parameter1=item.parameter1)
        items2 = ProductModel.objects.filter(parameter2=item.parameter2)
        items4 = ProductModel.objects.filter(parameter4=item.parameter4)
        items8 = ProductModel.objects.filter(parameter8=item.parameter8)
        items9 = ProductModel.objects.filter(category=item.category)
        return list(set(list(chain(items1, items2, items4, items8, items9))))

class RequestsView(View):
    def post(self, *args):
        context = {
            'categories': CategoryModel.objects.all(),
        }
        print(self.request.POST)
        data = self.request.POST
        name = data['name']
        car = data['car']
        text = data.get('text') if data.get('text') is not None else ' '
        acum = data.get('acum') if data.get('acum') is not None else ' '
        try:
            phone = str(data['phone']).replace('-', '').replace('+','').replace(' ', '')
            if phone.replace('+', '').isnumeric():
                request = RequestsModel(
                    name=name,
                    car_mark=car,
                    phone=phone,
                    problem=text,
                    acum=acum
                )
                request.save()
                
                text = f'Вам пришла новая заявка \nИмя заявки: {name} \nНомер телефона заявки: {phone} \nМарка авто заявки: {car}\nВыбранный товар: {acum}\nТекст заказчика: {text}'
                
                url = 'https://api.telegram.org/bot6993669434:AAGwSMLGIISh9yjjHZGZE5mBLzLiWpNTcxc/sendMessage'
                # 734715565
                
                data = urlencode({'chat_id': '734715565', 'text': f'{text}'}).encode()
                req = Request(url, data=data)
                urlopen(req)
                
                return render(self.request, template_name='main/thanks-page.html', context=context)
            else:
                return redirect('/error')
        except Exception as ex:
            print(ex, 'error')
            return redirect('/error')
