from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    """Главная страница."""
    return redirect('catalog')


def show_catalog(request):
    """Каталог."""
    template = 'catalog.html'
    sort_params = request.GET.get('sort', None)
    if sort_params is not None:
        if sort_params == 'name':
            phones = Phone.objects.order_by('name')
        elif sort_params == 'min_price':
            phones = Phone.objects.order_by('price')
        elif sort_params == 'max_price':
            phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.all()

    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    """Показать конкретный товар."""
    template = 'product.html'
    # получить все строки из таблицы Phone
    phone_db_response = Phone.objects.filter(slug=slug)
    for phone in phone_db_response:
        print(phone.name)
        print(phone.slug)
        print(phone.lte_exists)
    context = {
        'phone': phone
    }
    return render(request, template, context)
