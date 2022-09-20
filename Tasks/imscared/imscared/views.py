#This for default view or a home page
import re
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def home(request):
    '''name = request.GET.get('name')
    surname = request.GET.get('surname')'''
    return render(request,'hometemplate.html')
    #return HttpResponse('<a href="http://127.0.0.1:8000/testapp/">Go to testapp</a>')