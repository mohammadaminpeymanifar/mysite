from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index_view(Request):
    return HttpResponse ('<h1> Home page </h1>')

def aboute_view(Request):
    return HttpResponse ('<h1> About Page </h1>')

def contact_view(Request):
    return HttpResponse ('<h1> Contact Page </h1>')