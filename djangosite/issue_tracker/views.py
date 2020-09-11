from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html")


def signup(request):
    print(request.method)
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        context = {
            "form": form
        }
        if form.is_valid():
            form.save()
            return redirect("issues_home")
    else:
        form = UserCreationForm()
        context = {
            "form": form
        }
    return render(request, "registration/signup.html", context)

@login_required(login_url="login")
def secret(request):
    return render(request, "secret.html")