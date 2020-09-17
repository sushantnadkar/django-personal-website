from django.contrib import admin
from .models import Issue
from django_summernote.admin import SummernoteModelAdmin

class IssueAdmin(SummernoteModelAdmin):
    search_fields = ["title", "description"]
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("description",)

admin.site.register(Issue, IssueAdmin)
