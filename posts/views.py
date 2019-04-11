from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostModelForm
from .models import Post

# Create your views here.
def create(request):
    if request.method == "POST" :
        # 작성된 post를 DB에 적용
        form = PostModelForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('posts:list')
    else :
        # post를 작성하는 form을 보여 줌
        form = PostModelForm()
        return render(request, 'posts/create.html', {'form': form})

def list(request) :
    posts = Post.objects.all()
    return render(request,'posts/list.html', {'posts' : posts})
    
def delete(request, id) :
    post = get_object_or_404(Post, pk=id)

    if request.method=='POST' :
        post.delete()
        return redirect('posts:list')
    return redirect('posts:list')

    
def update(request, id) :
    post =  get_object_or_404(Post, pk=id)
    
    if request.method=='POST' :
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid() :
            form.save()
            return redirect('posts:list')
    
    form = PostModelForm(instance=post)
    return render(request,'posts/update.html',{'form': form})

