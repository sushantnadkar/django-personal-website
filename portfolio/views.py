from django.views import generic
from .models import Project
from .forms import ContactForm


class ProjectListAndContactForm(generic.ListView, generic.edit.FormView):
	queryset = Project.objects.all().order_by("category").filter(status=1)
	template_name = "portfolio.html"
	context_object_name = "projects"

	form_class = ContactForm
	success_url = "/#contact"
	object_list = None

	def form_valid(self, form):
		print("="*100,"\n",form.cleaned_data)
		form.send_email()
		return super(ProjectListAndContactForm, self).form_valid(form)
