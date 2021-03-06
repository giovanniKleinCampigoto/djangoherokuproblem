from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

class Subject(models.Model):
	name = models.CharField(max_length=200)
	color = models.CharField(max_length=7)

	def __str__(self):
		return self.name

class Author(models.Model):
	name = models.CharField(max_length=200)
	picture = CloudinaryField(blank=True)

	def __str__(self):
		return self.name

class Article(models.Model):
	title = models.CharField(max_length=200)
	slug = models.CharField(max_length=200)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	publish_date = models.DateTimeField(default=timezone.now)
	hero_image = CloudinaryField(blank=True);
	text = models.TextField()

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('publish_date',)
