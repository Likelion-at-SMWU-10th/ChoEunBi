from rest_framework import serializers
from .models import *

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'date', 'body')
    
class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'date', 'summary')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_at', 'updated_at', 'blog')
        read_only_fields = ('blog', ) # blog field는 읽기 전용으로 명시