from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.utils.text import slugify
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .forms import IssueForm
from .models import Issue


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

@login_required(login_url="login")
def create_issue(request):

    template_name = "issues/create.html"
    form_class = IssueForm
    context = {
        "form": form_class
    }
    if request.method == "POST":
        form = IssueForm(request.POST or None)

        if form.is_valid():
            new_issue = form.save(commit=False)
            new_issue.slug = slugify(form.cleaned_data["title"])
            new_issue.creator = request.user
            new_issue.status = 0
            new_issue.save()
            context["message"]="Issue created successfully!"

            return render(request, template_name, context)
    else:
        form = IssueForm()
    return render(request, template_name, context)

def list_issue(request):

    template_name = "issues/list.html"
    queryset = Issue.objects.all().order_by("-updated_on")
    context = {
        "issues": queryset
    }

    return render(request, template_name, context)

def issue_details(request, slug):

    queryset = get_object_or_404(Issue, slug=slug)
    template_name = "issues/details.html"
    context = {
        "issue": queryset
    }

    return render(request, template_name, context)

@login_required(login_url="login")
def update_issue(request, slug):

    context = {}
    template_name = "issues/update.html"
    queryset = get_object_or_404(Issue, slug=slug)
    form = IssueForm(request.POST or None, instance = queryset)
    context = {
        "form": form
    }

    if form.is_valid():
        form.save()

        return HttpResponseRedirect("/issues/" + slug)

    return render(request, template_name, context)

@login_required(login_url="login")
def delete_issue(request, slug):

    template_name = "issues/delete.html"
    queryset = get_object_or_404(Issue, slug=slug)
    context = {
        "issue": queryset
    }
    if request.method == "POST":
        queryset.delete()

        return redirect("list_issue")

    return render(request, template_name, context)