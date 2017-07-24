from rest_framework import serializers
from .models import Subject
from .models import Article


class SubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subject
		fields = ('name','color')

class ArticleSerializer(serializers.ModelSerializer):
	author = serializers.StringRelatedField(many=False, read_only=True)
	subject = serializers.StringRelatedField(many=False, read_only=True)

	class Meta:
		model = Article
		fields = ('slug','title','hero_image','author', 'subject', 'publish_date', 'text')