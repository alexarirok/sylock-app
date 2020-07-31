from django.shortcuts import render, redirect
from loanqualification.models import LoanQualification
from loanqualification.forms import LoanQualificationForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


def loanqualification(request):
    template = 'loanqualification.html'
    if request.method == 'POST':
        form = LoanQualificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = LoanQualificationForm
    return render(request, template, {'form':form})

