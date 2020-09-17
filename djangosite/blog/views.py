from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import generic
from django.core.paginator import Paginator
from .models import Post

def post_list(request):
	queryset = Post.objects.filter(status=1).order_by("-created_on")
	template_name = "blog/post_list.html"
	page = request.GET.get("page", 1)

	paginator = Paginator(queryset, 3)
	context = {}

	try:
		posts = paginator.page(page)
	except:
		posts = paginator.page(1)

	context["posts"] = posts

	return render(request, template_name, context)

def post_detail(request, slug):
	queryset = get_object_or_404(Post, slug=slug)
	template_name = "blog/post_detail.html"
	context = {
		"post": queryset
	}

	return render(request, template_name, context)
