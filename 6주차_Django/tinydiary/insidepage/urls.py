from django.urls import path
from insidepage import views

urlpatterns = [
    path('', views.index, name='index'),
    path('january/', views.january, name='january'),
    path('march/', views.march, name='march')
]