from .models import Product, Client, Order
from django.http import HttpResponse
import logging
import datetime

logger = logging.getLogger(__name__)


def links(request):
    logger.info(f'Transition on links, {datetime.datetime.now()}')
    return HttpResponse(
        "<title>Ссылочная2</title>"
        "<h3><a href='/product_reader/'>.....Товары.....</a></h3>"
        "<h3><a href='/client_reader/'>.....Клиенты.....</a></h3>"
        "<h3><a href='/order_reader/'>.....Заказы.....</a></h3>"
    )


def product_reader(request):
    logger.info(f'Transition on products, {datetime.datetime.now()}')
    return HttpResponse(Product.objects.all())


def client_reader(request):
    logger.info(f'Transition on list_clients, {datetime.datetime.now()}')
    return HttpResponse(Client.objects.all())


def order_reader(request):
    logger.info(f'Transition on orders, {datetime.datetime.now()}')
    return HttpResponse(Order.objects.all())

