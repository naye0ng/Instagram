from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model

# Create your views here.
def login(request) :
    if request.method == "POST":
        # POST : 실제 로그인(세션에 유저 정보 추가)
        form = AuthenticationForm(request, request.POST)
        if form.is_valid() :
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'posts:list')
    else:
        # GET : 로그인 정보 입려
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form}) 

def logout(request) :
    auth_logout(request)
    return redirect('posts:list')

def signup(request) :
    if request.method == "POST" :
        form = UserCreationForm(request.POST)
        if form.is_valid() :
            user = form.save()
            # 로그인처리까지하는데 이때 들어오는 password값은 2개가 들어오므로 user에서 받아온 결과물로 로그인 처리하자
            # auth_login(request, request.POST)
            auth_login(request, user)
            return redirect('posts:list')
    else :
        form = UserCreationForm() 
    return render(request, 'accounts/signup.html', {'form': form})
    
# 사용자 개인페이지
def people(request,username) :
    # 사용자에 대한 정보 
    people = get_object_or_404(get_user_model(),username=username)
    return render(request, 'accounts/people.html', {'people': poeple})