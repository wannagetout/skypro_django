from django.shortcuts import render


def main_catalog(request):
    return render(request, 'catalog/home.html')


def main_contacts(request):
    return render(request, 'catalog/contacts.html')
