from django.urls import path
from insidepage import views

urlpatterns = [
    path('', views.index, name='index'),
    path('january/', views.january, name='january'),
    path('march/', views.march, name='march'),
    path('month/<str:month>', views.month, name='month'),
    path('detail/<int:diary_id>', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('edit/', views.edit, name='edit'),
    path('update/<int:diary_id>', views.update, name='update'),
]