from django.views import generic
from .models import Project

class ProjectList(generic.ListView):
	queryset = Project.objects.filter(status=1)
	template_name = "portfolio.html"

