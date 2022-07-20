from django.urls import path
from .views import *

urlpatterns = [
    path('blog/', BlogList.as_view()),
    path('blog/<int:pk>', BlogDetail.as_view()),
    path('<int:blog_id>/comment', CommentList.as_view()), # 게시글에 댓글 작성, 게시글에 따른 댓글 리스트 가져오기
    path('comment/<int:comment_id>', CommentDetail.as_view()), # 특정 댓글 가져오기, 댓글 수정, 삭제
]