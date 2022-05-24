from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Oi')
    return render(request, 'base/home.html')
