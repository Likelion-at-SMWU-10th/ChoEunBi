from django.shortcuts import get_object_or_404, render
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
    months = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return render(request, 'insidepage/month.html', {'diaries': diaries, 'month': months[int(month)-1]})

def detail(request, diary_id):
    diary_detail = get_object_or_404(Diary, pk = diary_id)
    return render(request, 'insidepage/detail.html', {'diary': diary_detail})