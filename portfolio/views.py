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
		if form.is_valid():
			form.send_email()
			context["message"]="Email sent successfully!"

			return render(request, template_name, context)

	return render(request, template_name, context)