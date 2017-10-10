from django.shortcuts import render
from .forms import *
# Create your views here.


def landing(request):
    form = SubscriberForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        print(form.cleaned_data)
        newform = form.save()

    return render(request,'landing/landing.html',locals())