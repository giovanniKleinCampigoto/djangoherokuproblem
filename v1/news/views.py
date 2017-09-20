from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views import View
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from .models import Subject
from .serializers import SubjectSerializer
from rest_framework import filters
from rest_framework import generics
from rest_framework import viewsets

def subject_detail(request, pk):
	try:
	 	subject = Subject.objects.get(pk=pk)
	except Subject.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = SubjectSerializer(subject)
		return JsonResponse(serializer.data)

class ArticleFilteredList(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        subject = self.kwargs['subject']
        return Article.objects.filter(subject__name=subject)

def articles_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        ordering = ('publish_date',)
        return JsonResponse(serializer.data, safe=False)

def article_detail(request, pk):
	try:
	 	article = Article.objects.get(pk=pk)
	except Article.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = ArticleSerializer(article)
		return JsonResponse(serializer.data)
