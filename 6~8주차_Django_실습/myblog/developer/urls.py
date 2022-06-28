from unicodedata import name
from django.urls import path
from developer import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('detail/<int:blog_id>', views.detail, name='detail')
]