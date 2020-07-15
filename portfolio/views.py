from django.views import generic
from .models import Project

class ProjectList(generic.ListView):
	queryset = Project.objects.all().order_by("category").filter(status=1)
	template_name = "portfolio.html"
	context_object_name = "projects"
