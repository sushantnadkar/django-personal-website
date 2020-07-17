from . import views
from django.urls import path

urlpatterns = [
    path("", views.project_list, name="portfolio"),
]