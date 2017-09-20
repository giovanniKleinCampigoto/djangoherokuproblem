from rest_framework import serializers
from .models import Subject
from .models import Article
from .models import Author

class SubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subject
		fields = ('name','color')

class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = ('name','picture')

class ArticleSerializer(serializers.ModelSerializer):
	author = AuthorSerializer(many=False,read_only=True)
	subject = SubjectSerializer(many=False,read_only=True)
	
	class Meta:
		model = Article
		fields = ('slug','title','hero_image','author', 'subject', 'publish_date', 'text')
