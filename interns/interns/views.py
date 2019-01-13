from django.core.checks import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.mail import send_mail
from django.conf import settings

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("articles:list")
    else:
        form = UserCreationForm()

    return render(request, 'interns/signup.html', {'form': form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect("articles:list")

    else:
        form = AuthenticationForm()

    return render(request, 'interns/login.html', {'form': form})


def thankyou(request):
    form = signup(request.POST or None)
    save_it= form.save(commit=False)
    save_it.save()

    messages.success(request, "Thankyou")
    return HttpResponseRedirect('/thank-you/')
