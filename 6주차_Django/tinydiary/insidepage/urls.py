from django.urls import path
from insidepage import views

urlpatterns = [
    path('', views.index, name='index'),
    path('january/', views.january, name='january'),
    path('march/', views.march, name='march'),
    path('month/<str:month>', views.month, name='month'),
    path('detail/<int:diary_id>/', views.detail, name='detail'),
    path('detail/<int:diary_id>/<int:comment_id>', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('update/<int:diary_id>', views.update, name='update'),
    path('delete/<int:diary_id>', views.delete, name='delete'),
    path('search/', views.search, name='search'),
    path('commentcreate/<int:diary_id>', views.commentcreate, name='commentcreate'),
    path('commentdelete/<int:comment_id>', views.commentdelete, name='commentdelete'),
    path('commentupdate/<int:comment_id>', views.commentupdate, name='commentupdate')
]