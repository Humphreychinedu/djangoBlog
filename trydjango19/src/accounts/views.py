from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.shortcuts import render, redirect

from .forms import UserLoginForm, UserRegisterForm

# Create your views here.


def login_view(request):
    next = request.GET.get('next')
    title = "Login"
    template_name = "form.html"
    form = UserLoginForm(request.POST or None)
    context = {
        "form": form,
        "title": title
        }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect("next")
        return redirect("/")
    return render(request, template_name, context)


def register_view(request):
    next = request.GET.get('next')
    template_name = "form.html"
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    context = {
        "form": form,
        "title": title
        }
   
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
    login(request, new_user)
    if next:
        return redirect("next")
    return redirect("/")
    return render(request, template_name, context)


def logout_view(request):
    template_name = "form.html"
    logout(request)
    return redirect("/")
    return render(request, template_name, {})
