from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'

urlpatterns = [
    path('login/',views.login,name='login'),
    path('logout/',views.logout, name='logout'),
    path('signup/',views.signup, name='signup'),
    path('upadte/',views.update, name='update'),
    path('delete/',views.delete, name='delete'),
    path('passwd/',views.passwd, name='passwd'),
    path('accounts/<int:user_id>/follow/', views.follow, name='follow'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)