import json

from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        categories = []
        with open('data.json') as data:
            for item in json.load(data):
                categories.append(Category(**item))
        Category.objects.bulk_create(categories)

