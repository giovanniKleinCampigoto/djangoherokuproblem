from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from .models import Subject
from .serializers import SubjectSerializer

def subject_detail(request, pk):
	try:
	 	subject = Subject.objects.get(pk=pk)
	except Subject.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = SubjectSerializer(subject)
		return JsonResponse(serializer.data)

def articles_list(request):    
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

def article_detail(request, pk):
	try:
	 	article = Article.objects.get(pk=pk)
	except Article.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = ArticleSerializer(article)
		return JsonResponse(serializer.data)