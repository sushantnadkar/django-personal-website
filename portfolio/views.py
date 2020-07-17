from django.views import generic
from .models import Project
from .forms import ContactForm
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse


def project_list(request):
	queryset = Project.objects.all().order_by("category").filter(status=1)
	template_name = "portfolio.html"
	form_class = ContactForm
	context = {
		"projects": queryset,
		"form": form_class
	}

	if request.method == "POST":
		form = ContactForm(request.POST)
		context["message"] = "Email sent successfully!"
		if form.is_valid():
			form.send_email()
			return render(request, template_name, context)
	else:
		form = ContactForm()
		context["form"] = form
	return render(request, template_name, context)