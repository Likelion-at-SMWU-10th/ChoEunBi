from django.shortcuts import get_object_or_404, redirect, render
from .models import Diary
from .forms import DiaryForm, CommentModelForm
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
    form = CommentModelForm()
    return render(request, 'insidepage/detail.html', {'diary': diary_detail, 'form': form})

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
    month = request.GET.get('month', '')

    month_val_result = validate_month(month)
    # 1. month 에러 O, query 존재 X
    if month_val_result and not query:
        return render(request, 'insidepage/search.html', {'error': month_val_result['error'], 'guide': 'Enter something you want to find...'})
    # 2. month 에러 O, query 존재 O
    elif month_val_result and query:
        return render(request, 'insidepage/search.html', {'error': month_val_result['error']})
    # 3. month 에러 X, query 존재 X
    elif not month_val_result and not query:
        return render(request, 'insidepage/search.html', {'guide': 'Enter something you want to find...'})

    # 4. month 에러 X, query 존재 O
    if month == '': # month에 아무것도 입력되지 않은 경우
        diaries = (Diary.objects.filter(title__contains=query) | Diary.objects.filter(body__contains=query)).order_by("-pub_date")
        return render(request, 'insidepage/search.html', {'diaries': diaries})
    else: 
        diaries = (Diary.objects.filter(pub_date__month=int(month), title__contains=query) | Diary.objects.filter(pub_date__month=int(month), body__contains=query)).order_by("-pub_date")
        return render(request, 'insidepage/search.html', {'diaries': diaries})

def validate_month(month):
    # 1. 숫자가 아닌 타입이 입력된 경우
    try:
        month_int = int(month)
    except ValueError: 
        if month == '': # 1-1. 입력이 없는 경우[OK]
            return
        else: # 1-2. 숫자가 아닌 타입이 입력된 경우
            return {'error': 'Only numbers must be entered in Month'}
    
    # 2. 1 ~ 12 사이의 숫자가 아닌 경우
    if month_int<1 and month_int>12: # 1~12사이의 숫자가 아닌 경우
        return {'error': 'Only numbers between 1 and 12 must be entered in Month'}
    # 3. 1 ~ 12 사이의 숫자인 경우[OK]
    return

def commentcreate(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.diary = diary
            comment.save()
            return redirect('detail', diary_id=diary.pk)
    
    return redirect('detail', diary_id=diary.pk)
