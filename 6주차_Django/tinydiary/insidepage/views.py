from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def january(request):
    return render(request, 'january.html')

def march(request):
    return render(request, 'march.html')
