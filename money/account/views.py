# Create your views here.

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist

def createUser(req):
    if req.method == 'POST':
        username = req.POST['username']
        email = req.POST['username']
        passowrd = req.POST['password']
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        
        u = User.objects.filter(username__exact = username)
        if len(u) != 0:
            return HttpResponse('user exist')

        user = User.objects.create_user(username, username, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        req.session.set_expiry(0)
        login(req, user)
        return HttpResponse('OK')  # return to user main page  


def login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        is_saved = req.POST['is_saved']
        if is_saved == '0':                    #check the actual value.
            req.session.set_expiry(0)
        user = authenticate(username = username, password = password)
        if user is not None:
            login(req, user)
            if req.GET.has_key('next'):
                return HttpResponseRedirect(req.POST['next'])
            else:
                return HttpResponse('OK') # return to user main page
        else:
            return HttpResponse('failed')


def logout(req):
    return HttpResponseRedirect('../index.html')
                                                                                  