from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Profile

# UserChangeForm을 상속받아서 재정의
class CustomUserChangeForm(UserChangeForm) :
    class Meta :
        model = get_user_model()
        fields = ['username','email','last_name','first_name']

class CustomUserCreationForm(UserCreationForm) :
    class Meta(UserCreationForm.Meta) :
        model = get_user_model()


class ProfileForm(forms.ModelForm) :
    class Meta :
        model = Profile
        fields = ['description','nickname','userimage']
