from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import main_catalog, main_contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', main_catalog),
    path('contacts', main_contacts),
]
