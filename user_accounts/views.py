from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .forms import FileForm


def home(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.uploaded_by = request.user
            form.save()
            messages.success(request, 'File uploaded successfully!')
            return redirect('home')
        else:
            messages.error(request, 'File not uploaded!')
            return redirect('home')
    else:
        form = FileForm()
    return render(request, 'home.html', {
        'form': form
    })


def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'user_accounts/Signup.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')###todo: set
        else:
            return render (request,'user_accounts/Signup.html', {'error':'Password does not match!'})
    else:
        return render(request,'user_accounts/Signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render (request,'user_accounts/Login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'user_accounts/Login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('login')

