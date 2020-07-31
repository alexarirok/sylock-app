from django.shortcuts import render, redirect
from profiles.models import Profile
from profiles.forms import ProfileForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect



def base(request):
    template = 'base.html'
    return render(request, template, { })

def profile(request):
    template = 'profile.html'
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm
    return render(request, template, {'form':form})

