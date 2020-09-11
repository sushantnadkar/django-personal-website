from djangosite.issue_tracker import views
from django.urls import path, include


# app_name = "issues"
urlpatterns = [
    path("", views.home, name="issues_home"),
    path("signup/", views.signup, name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("secret/", views.secret, name="secret"),
]