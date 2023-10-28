from django.core.management.base import BaseCommand
from myapp2.models import Product
from random import choice as ch, randint as ri, uniform as ui
from datetime import datetime as dt


class Command(BaseCommand):
    help = "Create product."

    def add_arguments(self, parser):
        parser.add_argument('start', type=int, help='start_number_range')
        parser.add_argument('end', type=int, help='end_number_range')

    def handle(self, *args, **kwargs):
        for i in range(1, 201):
            product = Product(title=f'product{i}', description=f'this is product {i}',
                              price=round(ui(0.01, 100.01), 2), count=100, date_add=dt.now())
            product.save()
            self.stdout.write(f'{product}')
