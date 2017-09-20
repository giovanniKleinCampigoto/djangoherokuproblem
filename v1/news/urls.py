
from django.conf.urls import url

from . import views
from news.views import ArticleFilteredList

urlpatterns = [
	url(r'^news/subject/(?P<pk>[0-9]+)/$', views.subject_detail),
    url(r'^news/articles$', views.articles_list),
    url(r'^news/articles/(?P<pk>[0-9]+)/$', views.article_detail),
	url('^news/articles/(?P<subject>.+)/$', ArticleFilteredList.as_view()),
]
