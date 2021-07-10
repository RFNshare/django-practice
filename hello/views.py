from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def myview(request):
    resp = HttpResponse('C is for cookie and that is good enough for me...')
    resp.set_cookie('dj4e_cookie', '579036d9', max_age=1000)
    return resp
