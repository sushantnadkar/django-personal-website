from . import views
from django.urls import path

urlpatterns = [
    path("", views.ProjectListAndContactForm.as_view(), name="portfolio"),
]