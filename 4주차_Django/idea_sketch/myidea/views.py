from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contents1(request):
    return render(request, 'contents_1.html')

def contents2(request):
    return render(request, 'contents_2.html')
