from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .serializers import *
from .models import *

class BlogList(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogListSerializer(blogs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogDetail(APIView):
    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    
    def put(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        blog = self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentList(APIView):
    # /<int:blog_id>/comment
    # 특정 게시글에 따른 댓글 
    def get(self, request, blog_id):
        comments = Comment.objects.filter(blog=blog_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    # /<int:blog_id>/comment/
    def post(self, request, blog_id):
        blog = get_object_or_404(Blog, pk=blog_id)
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(blog=blog)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    # /comment/<int:comment_id>
    # 특정 댓글 가져오기
    def get(self, request, comment_id):
        comments = self.get_object(comment_id)
        serializer = CommentSerializer(comments)
        return Response(serializer.data)
    
    # 댓글 수정하기
    def put(self, request, comment_id):
        comment = self.get_object(comment_id)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # 댓글 삭제하기
    def delete(self, request, comment_id):
        comment = self.get_object(comment_id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

            