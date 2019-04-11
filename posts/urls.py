from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('create/', views.create, name='create'),
<<<<<<< HEAD
    path('', views.list, name='list'),
    path('<int:id>/delete',views.delete, name='delete'),
    path('<int:id>/update', views.update, name='update'),
=======
>>>>>>> b5436e9d3d9f93fa3c0e5215ab95dfceb90a4dd6
]