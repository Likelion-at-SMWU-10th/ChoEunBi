from django.shortcuts import get_object_or_404, redirect, render
from .models import Diary, Comment
from .forms import CommentModelForm, DiaryModelForm

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

def detail(request, diary_id, comment_id=None):
    diary_detail = get_object_or_404(Diary, pk = diary_id)

    if comment_id==None:  
        form = CommentModelForm()
        return render(request, 'insidepage/detail.html', {'diary': diary_detail, 'form': form})
    else:
        comment = get_object_or_404(Comment, pk = comment_id)
        form = CommentModelForm(instance=comment)
        return render(request, 'insidepage/detail.html', {'diary': diary_detail, 'form': form, 'comment': comment})
        

def create(request):
    if request.method == 'POST':
        form = DiaryModelForm(request.POST)
        if form.is_valid():
            diary = form.save()
            return redirect('detail', diary_id=diary.pk)

    if request.method == 'GET':
        form = DiaryModelForm()
    return render(request, 'insidepage/create.html', {'form': form})

def update(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    if request.method == 'POST':
        form = DiaryModelForm(request.POST, instance=diary)
        if form.is_valid():
            form.save()
            return redirect('detail', diary_id=diary.pk)
    else:
        form = DiaryModelForm(instance=diary)
        return render(request, 'insidepage/edit.html', {'form':form, 'diary_id':diary_id})

def delete(request, diary_id):
    post = get_object_or_404(Diary, pk=diary_id)
    month = post.pub_date.month
    post.delete()
    return redirect('month', month=month)

def search(request):
    query = request.GET.get('query', '')
    month = request.GET.get('month', '')

    month_val_result = validate_month(month)
    # 1. month ?????? O, query ?????? X
    if month_val_result and not query:
        return render(request, 'insidepage/search.html', {'error': month_val_result['error'], 'guide': 'Enter something you want to find...'})
    # 2. month ?????? O, query ?????? O
    elif month_val_result and query:
        return render(request, 'insidepage/search.html', {'error': month_val_result['error']})
    # 3. month ?????? X, query ?????? X
    elif not month_val_result and not query:
        return render(request, 'insidepage/search.html', {'guide': 'Enter something you want to find...'})

    # 4. month ?????? X, query ?????? O
    if month == '': # month??? ???????????? ???????????? ?????? ??????
        diaries = (Diary.objects.filter(title__contains=query) | Diary.objects.filter(body__contains=query)).order_by("-pub_date")
        return render(request, 'insidepage/search.html', {'diaries': diaries})
    else: 
        diaries = (Diary.objects.filter(pub_date__month=int(month), title__contains=query) | Diary.objects.filter(pub_date__month=int(month), body__contains=query)).order_by("-pub_date")
        return render(request, 'insidepage/search.html', {'diaries': diaries})

def validate_month(month):
    # 1. ????????? ?????? ????????? ????????? ??????
    try:
        month_int = int(month)
    except ValueError: 
        if month == '': # 1-1. ????????? ?????? ??????[OK]
            return
        else: # 1-2. ????????? ?????? ????????? ????????? ??????
            return {'error': 'Only numbers must be entered in Month'}
    
    # 2. 1 ~ 12 ????????? ????????? ?????? ??????
    if month_int<1 and month_int>12: # 1~12????????? ????????? ?????? ??????
        return {'error': 'Only numbers between 1 and 12 must be entered in Month'}
    # 3. 1 ~ 12 ????????? ????????? ??????[OK]
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

def commentdelete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('detail', diary_id=comment.diary.pk)

def commentupdate(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        form = CommentModelForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('detail', diary_id=comment.diary.pk)
    else:
        # form = CommentModelForm(instance=comment)
        return redirect('detail', diary_id=comment.diary.pk, comment_id=comment_id)