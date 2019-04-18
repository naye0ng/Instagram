from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, update_session_auth_hash
from .forms import CustomUserChangeForm, ProfileForm, CustomUserCreationForm
from .models import Profile

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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid() :
            user = form.save()
            # 매 회원가입때마다 profile 테이블도 생성
            Profile.objects.create(user=user)
            auth_login(request, user)
            return redirect('posts:list')
    else :
        form = CustomUserCreationForm() 
    return render(request, 'accounts/signup.html', {'form': form})
    
# 사용자 개인페이지
def people(request,username) :
    # 사용자에 대한 정보 
    people = get_object_or_404(get_user_model(),username=username)
    return render(request, 'accounts/people.html', {'people': people})
    
# 회원 정보 변경
def update(request) :
    if request.method == 'POST' :
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)

        if user_change_form.is_valid() and profile_form.is_valid() :
            # 객체가 저장되고 난 후의 값을 반환한다.
           user = user_change_form.save()
           profile_form.save()
           return redirect('people', user.username)
        
    else :
        # 변경될 사용자의 정보를 같이 넘겨줘야 한다.
        user_change_form = CustomUserChangeForm(instance=request.user)
        # instance에 넣어줄 정보가 있는 user도 있고, 없는 user도 있다.
        profile, create = Profile.objects.get_or_create(user = request.user)
        profile_form = ProfileForm(instance=profile)
        
        context={
            'user_change_form' : user_change_form,
            'profile_form' : profile_form,
        }
        return render(request,'accounts/update.html',context)
    
# 비밀 번호 변경
def passwd(request) :
    if request.method == "POST" :
        passwd_change_form = PasswordChangeForm(request.user, request.POST)
        if passwd_change_form.is_valid() :
            passwd_change_form.save()
            # 세션 업데이트 및 유지
            update_session_auth_hash(request, passwd_change_form.user)
            return redirect('people', request.user.username)
    else :
       passwd_change_form = PasswordChangeForm(request.user) 
       return render(request, 'accounts/passwd.html',{'passwd_change_form' : passwd_change_form})

# 회원 탈퇴
def delete(request) :
    if request.method == "POST" :
        request.user.delete()
        return redirect('accounts:signup')
    return render(request,'accounts/delete.html')
    
def follow(request, user_id) :
    person = get_object_or_404(get_user_model(), pk=user_id)
    # 만약 현재 유저(request.user)가 해당유저(user)를 팔로잉하고 있었다면, 팔로우 취소
    if request.user in person.followers.all() :
        person.followers.remove(user=request.user) 
    else :
        person.followers.add(request.user)
    return redirect('people', person.username)
    
    
    