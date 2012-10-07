# Create your views here.
from money.Account.models import UserInfo
from money.Utils.constants import STATE
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


def createuser(req): #/accounts/newuser/
    # form class of the view
    class _NewUserForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ('username','password','email','first_name','last_name')
            widgets = {'password':forms.PasswordInput,}

    if req.method == 'POST':
        newuserform = _NewUserForm(req.POST)
        if newuserform.is_valid():
            username = newuserform.cleaned_data['username']
            # create a new user
            # check whether a user does exist
            u = User.objects.filter(username__exact = username)
            if len(u) == 0:
                return HttpResponseRedirect('/user_not_exist_error.html')
            user = newuserform.save()
            req.session.set_expiry(0)
            login(req,user)
            return HttpResponseRedirect('/new_user_success.html')
        else:
            return HttpResponseRedirect('/accounts/createuser/')
    else:
        newuserform = _NewUserForm()
        return render_to_response('new_user.djhtml',{'form':newuserform},
                                  context_instance=RequestContext(req))


@receiver(post_save, sender=User)
def createUserInfo(sender, instance, created, **kwargv):
    if created:
        UserInfo.objects.create(user=instance)


@login_required    # /accounts/login/
def updateUserInfo(req): #/accounts/updateuserinfo/
    # update User Form class
    class _UpdateUserInfoForm(forms.Form):
        password = forms.CharField(widget=forms.PasswordInput,required=False)
        email = forms.EmailField(required=False)
        first_name = forms.CharField(required=False,max_length=30)
        last_name = forms.CharField(required=False,max_length=30)
        homeaddr = forms.CharField(required=False,max_length=30)
        state = forms.ChoiceField(required=False,choice=STATE)
        country = forms.CharField(required=False,max_length=20)
        contact = forms.CharField(required=False,max_length=16)

    if req.method == 'POST':
        if req.POST['password'] != '':
            req.user.set_password(req.POST['password'])
        if req.POST['email'] != '':
            req.user.email = req.POST['email']
        if req.POST['first_name'] != '':
            req.user.first_name = req.POST['first_name']
        if req.POST['last_name'] != '':
            req.user.last_name = req.POST['last_name']
        if req.POST['password'] != '' or req.POST['email'] != '' or req.POST['first_name'] != '' or req.POST['last_name'] != '':
            req.user.save()

        homeaddr = req.POST['homeaddr']
        state = req.POST['state']
        country = req.POST['country']
        contact = req.POST['contact']

        if homeaddr != '':
            user_info.homeaddr = homeaddr
        if state != '':
            user_info.state = state
        if country != '':
            user_info.country = country
        if contact != '':
            user_info.contact = contact
        if homeaddr != '' or state != '' or country != '' or contact != '':
            user_info.save()
        return HttpResponseRedirect('/update_userinfo_success,html')
    else:
        try:
            user_info = req.user.get_profile()
        except ObjectDoesNotExist:
            return HttpResponseRedirect('/user_not_found.html')
        
        updateuserinfoform = _UpdateUserInfoForm()
        return render_to_response('update_user_info.djhtml',
                                  {'form':updateuserinfoform, 'user_info':user_info, 'user':req.user},
                                  context_instance=RequestContext(req))


@login_required
def getUserInfo(req): #/accounts/user_info/
    try:
        user_info = req.user.get_profile()
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/user_not_found.html')
    return render_to_response('user_info.djhtml',
                              {'user_info':user_info, 'user':req.user},
                              RequestContext(req))


def login(req): #/accounts/login/
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
                return HttpResponseRedirect(req.GET['next'])
            else:
                return render_to_response('user_info.djhtml',
                                          {'user_info':user_info,'user':user},
                                          RequestContext(req))
        else:
            return HttpResponseRedirect('/login_fail.html')
    else:
        class _LoginForm(forms.Form):
            username = forms.CharField(max_length=30)
            password = forms.CharField(widget=forms.PasswordInput)
            is_saved = forms.BooleanField(required=False)

        loginform = _LoginForm()
        return render_to_response('login.djhtml',{'form':loginform,})


def logout(req): # /accounts/logout/
    logout(req)
    # redirect to login
    return HttpResponseRedirect('http://money.tinytractorlab.net/accounts/login/')
