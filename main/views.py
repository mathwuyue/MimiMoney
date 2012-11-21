# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

@login_required(login_url='../index.html')
def main(req):
    return render_to_response('main.djhtml',{})
