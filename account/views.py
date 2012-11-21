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
from django.http import HttpResponse

def createUser(req):
    if req.method == 'POST':
        username = req.POST['username']
        email = req.POST['username']
        password = req.POST['password']
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        
        u = User.objects.filter(username__exact = username)
        if len(u) != 0:
            return HttpResponse('failed')

        user = User.objects.create_user(username, username, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        req.session.set_expiry(0)
        return HttpResponse('success')  # return to user main page  


def userLogin(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        if req.POST.has_key('is_saved') :
            is_saved = req.POST['is_saved']
        else:
            is_saved = '0'
        if is_saved == '0' or is_saved == 'off':                    #check the actual value.
            req.session.set_expiry(0)
        else:
            req.session.set_expiry(300000)
        user = authenticate(username = username, password = password)
        if user is not None:
            login(req, user)
            if req.GET.has_key('next'):
                return HttpResponseRedirect(req.POST['next'])
            else:
                return HttpResponse('success') # return to user main page
        else:
            return HttpResponse('failed')


def userLogout(req):
    logout(req, '../index.html')
