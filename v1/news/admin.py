from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Subject)

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('name',)
@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('id','title','subject','publish_date','author')