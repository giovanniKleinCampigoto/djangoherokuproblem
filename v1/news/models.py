from django.db import models
from django.utils import timezone

# Create your models here.
class Subject(models.Model):
	name = models.CharField(max_length=200)
	color = models.CharField(max_length=7)

	def __str__(self):
		return self.name

class Author(models.Model):
	name = models.CharField(max_length=200)
	picture = models.ImageField(upload_to='pictures/%Y%m%d')

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name

class Article(models.Model):
	title = models.CharField(max_length=200)
	slug = models.CharField(max_length=200)
	author =  models.ForeignKey(Author, on_delete=models.CASCADE)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
	publish_date = models.DateTimeField(default=timezone.now)
	hero_image = models.ImageField(upload_to='pictures/%Y%m%d', blank=True)
	text = models.TextField()

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ('title',)
