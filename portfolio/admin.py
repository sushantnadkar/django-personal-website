from django.contrib import admin
from .models import Project, Category
from django_summernote.admin import SummernoteModelAdmin

class ProjectAdmin(SummernoteModelAdmin):
    search_fields = ["title", "description"]
    summernote_fields = ("description",)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)