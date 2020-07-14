from django.db import models


class Category(models.Model):
	title = models.CharField(max_length=100)

	def __str__(self):
		return self.title

	@classmethod
	def get_default_pk(cls):
		cat, created = cls.objects.get_or_create(title = "Other", defaults=dict( title="Other" ))
		return cat.pk

class Project(models.Model):

	STATUS = ((0, "On going"), (1, "Completed"))

	title = models.CharField(max_length=200)
	category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=Category.get_default_pk)
	url = models.URLField(max_length=200, null=True, blank=True)
	image = models.ImageField(upload_to="portfolio/projects/", null=True, blank=True)
	status = models.IntegerField(choices=STATUS, default=0)
	description = models.TextField()
	
	def __str__(self):
		return self.title

	class Meta:
		ordering = ["category"]