# Create your views here.

from shopping.models import ShoppingData
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


@login_required(login_url='../index.html')
def shopping(req):
    if req.method == 'POST':
        user = req.user
        title = req.POST['title']
        price = req.POST['price']
        currency = req.POST['currency']
        paying_type = req.POST['paying_type']
        shopping_type = req.POST['shopping_type']
        shop_name = req.POST['shop_name']
        rank = req.POST['rank']
        description = req.POST['description']

        newData = ShoppingData(title=title,price=price,currency=currency,shopping_type=shopping_type,shop_name=shop_name,rank=rank,description=description,paying_type=paying_type,user=user)
        newData.save()

        return render_to_response('add-result.djhtml', {'title': title, 'price': price, 'currency': currency, 'paying_type': paying_type,'shopping_type': shopping_type, 'shop_name': shop_name, 'rank': rank, 'description': description, 'date': newData.date, 'host': req.get_host()})
    else:
        return render_to_response('shopping.djhtml', {})
