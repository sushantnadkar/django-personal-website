from django.db import models
from django.contrib.auth.models import User

class Issue(models.Model):

	STATUS = ((0, "New Issues"), (1, "Icebox"), (2, "Backlog"), (3, "In Progress"), (4, "Review/QA"), (5, "Closed"))

	title = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(max_length=200, unique=True)
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	status = models.IntegerField(choices=STATUS, default=0)

	class Meta:
		ordering = ["-created_on"]

	def __str__(self):
		return self.title