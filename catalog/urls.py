from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import main_catalog, main_contacts, item_cards, item

app_name = CatalogConfig.name

urlpatterns = [
    path('', main_catalog),
    path('contacts/', main_contacts),
    path('items/', item_cards),
    path('item/<int:id>', item)
]
