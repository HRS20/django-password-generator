from django.shortcuts import render
import random
# from django.http import HttpResponse

# Create your views here.


# def home(request):
#     return HttpResponse('Working')

def home(request):
    return render(request,'generator/home.html')

def password(request):
    length=int(request.GET.get('length'))
    chars=list('abcdefghijklmnopqrstuvwxyz')
    my_pass=''
    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('specialchar'):
        chars.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        chars.extend(list('0123456789'))
    for i in range(length):
        my_pass+=random.choice(chars)

    return render(request,'generator/password.html',{'password':my_pass})

def about(request):
    return render(request,'generator/about.html')