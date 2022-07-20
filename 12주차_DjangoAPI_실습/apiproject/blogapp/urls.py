from django.urls import path
from .views import *

urlpatterns = [
    path('blog/', BlogList.as_view()),
    path('blog/<int:pk>', BlogDetail.as_view()),
    path('comment/', CommentList.as_view()),
    path('comment/<int:blog_id>', CommentList.as_view()),
]