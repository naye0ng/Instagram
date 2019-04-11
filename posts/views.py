from django.shortcuts import render, redirect
from .forms import PostModelForm
<<<<<<< HEAD
from .models import Post
=======
>>>>>>> b5436e9d3d9f93fa3c0e5215ab95dfceb90a4dd6

# Create your views here.
def create(request):
    if request.method == "POST" :
        # 작성된 post를 DB에 적용
        form = PostModelForm(request.POST)
        if form.is_valid() :
            form.save()
<<<<<<< HEAD
            return redirect('posts:list')
=======
            return redirect('post:create')
>>>>>>> b5436e9d3d9f93fa3c0e5215ab95dfceb90a4dd6
    else :
        # post를 작성하는 form을 보여 줌
        form = PostModelForm()
        return render(request, 'posts/create.html', {'form': form})

<<<<<<< HEAD
def list(request) :
    posts = Post.objects.all()
    return render(request,'posts/list.html', {'posts' : posts})
    
def delete(request, id) :
    post = Post.objects.get(pk=id)

    if request.method=='POST' :
        post.delete()
        return redirect('posts:list')
    return redirect('posts:list')

    
def update(request, id) :
    post = Post.objects.get(pk=id)
    
    if request.method=='POST' :
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid() :
            form.save()
            return redirect('posts:list')
    
    form = PostModelForm(instance=post)
    return render(request,'posts/update.html',{'form': form})
=======
>>>>>>> b5436e9d3d9f93fa3c0e5215ab95dfceb90a4dd6
