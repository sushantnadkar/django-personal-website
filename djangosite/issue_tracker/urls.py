from djangosite.issue_tracker import views
from django.urls import path, include


# app_name = "issues"
urlpatterns = [
    path("", views.home, name="issues_home"),
    path("signup/", views.signup, name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("secret/", views.secret, name="secret"),
    path("create/", views.create_issue, name="create_issue"),
    path("list/", views.list_issue, name="list_issue"),
    path("update/<slug:slug>/", views.update_issue, name="update_issue"),
    path("delete/<slug:slug>/", views.delete_issue, name="delete_issue"),
    path("<slug:slug>/", views.issue_details, name="issue_details"),
]