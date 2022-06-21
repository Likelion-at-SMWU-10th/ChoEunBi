from django.shortcuts import render
from .models import Diary

# Create your views here.
def index(request):
    return render(request, 'insidepage/index.html')

def january(request):
    return render(request, 'insidepage/january.html')

def march(request):
    return render(request, 'insidepage/march.html')

def month(request, month):
    diaries = Diary.objects.filter(pub_date__month=month)
    return render(request, 'insidepage/month.html', {'diaries': diaries})