from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'coverpage/home.html')

def about(request):
    return render(request, 'coverpage/about.html')