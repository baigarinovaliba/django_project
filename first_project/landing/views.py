from django.shortcuts import render
from .forms import SubscriberForm
# Create your views here.


def landing(request):
    name='I nada mas'
    form = SubscriberForm(request.POST or None)

    if request.method =="POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data['name'])
        new_form = form.save()

    return  render(request,'landing/landing.html',locals())