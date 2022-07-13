from django.shortcuts import get_object_or_404, redirect, render
from .models import Diary
from .forms import DiaryForm
from django.utils import timezone
from django.urls import reverse

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

def create(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        now = timezone.now()
        if form.is_valid():
            post = Diary()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.date = now
            post.save()
            return redirect('index')

    if request.method == 'GET':
        form = DiaryForm()
        return render(request, 'insidepage/create.html', {'form': form})

def search(request):
    query = request.GET.get('query', '')
    if query:
        diaries = Diary.objects.filter(title__contains=query)
        return render(request, 'insidepage/search.html', {'diaries': diaries})
    else:
        return render(request, 'insidepage/search.html', {'guide': 'Enter something you want to find...'})