from django.core.management.base import BaseCommand
from myapp2.models import Order, Client, Product
from random import choice as ch, randint as ri, uniform as ui
from datetime import datetime as dt


class Command(BaseCommand):
    help = "Create order."

    def handle(self, *args, **kwargs):
        for i in range(1, 21):
            customer = Client.objects.filter(pk=i).first()
            x = ri(1, 4)
            product_id = []
            total_price = 0
            for el in range(0, x):
                product = Product.objects.filter(pk=ri(1, 201)).first()
                if product.count > 0:
                    Product_id.append(product.id)
                    total_price += product.price
                    product.count -= 1
                    product.save()
            order = Order(customer=customer, total_price=round(total_price, 2))
            order.save()
            for el in product_id:
                order.products.add(Product.objects.filter(pk=el).first())
            self.stdout.write(f'{order}')
