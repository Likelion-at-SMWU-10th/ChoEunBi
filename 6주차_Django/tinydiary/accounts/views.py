from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['userId'])
                return render(request, 'accounts/signup.html', {'error': 'Existing user ID'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username = request.POST['userId'],
                    password = request.POST['password1']
                )
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Password Confirmation error'})
    else:
        return render(request, 'accounts/signup.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
