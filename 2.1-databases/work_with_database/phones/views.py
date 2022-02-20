from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    """Главная страница."""
    return redirect('catalog')


SORT_MAP = {
    'name': 'name',
    'min_price': 'price',
    'max_price': '-price',
}


def show_catalog(request):
    """Каталог."""
    template = 'catalog.html'
    sort_params = request.GET.get('sort', None)
    if sort_params is not None:
        phones = Phone.objects.order_by(SORT_MAP[sort_params])
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
