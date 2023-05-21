from django.shortcuts import render

from catalog.models import Product


def main_catalog(request):
    return render(request, 'catalog/home.html')


def main_contacts(request):
    return render(request, 'catalog/contacts.html')


def item_cards(request):
    context = {
        'title': 'Товары',
        'items': Product.objects.all()
    }
    return render(request, 'catalog/items.html', context)


def item(request, id: int):
    context = {
        'item': Product.objects.get(pk=id)
    }
    return render(request, 'catalog/item_card.html', context)
