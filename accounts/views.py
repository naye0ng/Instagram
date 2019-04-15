from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


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
