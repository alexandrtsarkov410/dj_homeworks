from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_by = request.GET.get('sort', 'name')
    phones = Phone.objects.all()
    if sort_by == 'name':
        phones = phones.order_by('name')
    elif sort_by == 'min_price':
        phones = phones.order_by('price')
    elif sort_by == 'max_price':
        phones = phones.order_by('-price')
    else:
        phones = phones.order_by('name')

    context = {
        'phones': phones,
        'current_sort': sort_by
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug__contains=slug).first()
    context = {'phone': phone}
    return render(request, template, context=context)
