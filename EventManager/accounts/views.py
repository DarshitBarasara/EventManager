from django.shortcuts import render,redirect
from django.http import HttpResponse

from .form import EventRegistrationForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

def event_registration(request):
    event = EventRegistrationForm()
    if request.method=="POST":
        event = EventRegistrationForm(request.POST)
        if event.is_valid():
            event.save()
            return redirect('/')

    context={'event': event}
    return render(request, 'E_R.html', context)

def participant_registration(request):
    participant = EventRegistrationForm()

    return render(request, 'P_R.html')
