from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'date', 'body')
    
class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'date', 'summary')