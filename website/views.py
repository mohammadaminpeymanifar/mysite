from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.http.response import HttpResponseRedirect
from django.contrib import messages
#----------------------------------------------------------------------------------------------
from website.forms import NameForm , contactForm , NewsletterForm

# Create your views here.

def index_view(request):
    return render (request ,'website/index.html')

def about_view(request):
    return render (request , 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submit successfully')
        else:
            messages.add_message(request,messages.ERROR,'your ticket didnot submit')
    form = contactForm()
    return render (request ,'website/contact.html',{'form':form})

#---------------------------------------------------------------------------------------------
def Newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

#---------------------------------------------------------------------------------------------
def test_view(request):
    if request.method == 'POST':                       # اگر کاربر فرم را Submit کرده باشد
        form = contactForm(request.POST)               # دریافت اطلاعات ارسال شده از فرم
        if form.is_valid():                            # اعتبارسنجی داده های فرم
            form.save()                                # ذخیره رکورد در دیتابیس
            return HttpResponse('done')                # نمایش پاسخ موفقیت
        else:
            return HttpResponse('not valid')           # در صورت نامعتبر بودن داده ها

    form = contactForm()                               # درخواست GET (اولین بار که صفحه باز می شود)
    return render(request,'test.html',{'form':form})   # ارسال فرم به قالب