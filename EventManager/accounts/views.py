from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'accounts/index.html')

def event_registration(request):
    return render(request, 'accounts/E_R.html')
