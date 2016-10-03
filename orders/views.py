from django.shortcuts import render
from django.http import HttpResponse

from orders.models import Order
import json


def index(request):
    # one_order = Order(company_name="Apple", quantity=10000)
    # one_order.save()

    # one_order = Order.objects.get(company_name="Apple")
    orders = Order.objects.filter(company_name="Apple")
    t = orders[0].json_object()

    return HttpResponse("this quantity is {}".format(t))
