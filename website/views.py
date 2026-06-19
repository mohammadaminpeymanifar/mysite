from django.shortcuts import render

# Create your views here.

def index_view(Request):
    return render (Request ,'website/index.html')

def aboute_view(Request):
    return render (Request , 'website/aboute.html')

def contact_view(Request):
    return render (Request ,'website/contact.html')