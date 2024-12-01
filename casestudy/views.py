from django.http import HttpResponse

from django.shortcuts import render


def home(request) :
    return render(request, 'website/index.html')

def about(request) :
    return HttpResponse("Hello World i am using django at about section")

def contact(request) :
    return HttpResponse("Hello World i am using django at contact section")