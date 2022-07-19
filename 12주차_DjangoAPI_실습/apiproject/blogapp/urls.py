from django.urls import path
from .views import BlogDetail, BlogList

urlpatterns = [
    path('blog/', BlogList.as_view()),
    path('blog/<int:pk>', BlogDetail.as_view()),
]