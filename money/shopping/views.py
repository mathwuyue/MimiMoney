# Create your views here.

from money.shopping.models import ShoppingData
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


def Shopping(req):
    if req.method == 'POST':
        return HttpResponse('ok')
