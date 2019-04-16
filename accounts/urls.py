from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/',views.login,name='login'),
    path('logout/',views.logout, name='logout'),
    path('signup/',views.signup, name='signup'),
    path('upadte/',views.update, name='update'),
    path('delete/',views.delete, name='delete'),
    path('passwd/',views.passwd, name='passwd'),
]