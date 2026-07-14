from django.shortcuts import render

# Create your views here.


def login_view(request):
    if request.user.is_authenticated:
        message = f'user is authenticated as {request.user.username}'
    else:
        message = 'user is not authenticated'
    return render (request,'accounts/login.html',{'message':message})


# def logout_view(request):
#    return render (request,'accounts/logout.html')


def singup_view(request):
    return render (request,'accounts/singup.html')
