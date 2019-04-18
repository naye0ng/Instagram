from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import PostModelForm, CommentModelForm
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Q

# Create your views here.
def create(request):
    if request.method == "POST" :
        # 작성된 post를 DB에 적용
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid() :
            post = form.save(commit=False)
            post.user = request.user
            form.save()
            return redirect('posts:list')
    else :
        # post를 작성하는 form을 보여 줌
        form = PostModelForm()
        return render(request, 'posts/create.html', {'form': form})

def list(request) :
    posts = []
    if not request.user.is_anonymous :
        # 내가 팔로우한 사람들의 post를 보여준다.
        # follow_posts = Post.objects.filter(user_id__in= request.user.followings.all())
    
        # (+) 내가 쓴 post 목록을 보여준다.
        # my_posts = request.user.post_set.all()
        # posts = follow_posts | my_posts
        posts = Post.objects.filter(Q(user_id__in= request.user.followings.all()) | Q(user=request.user))

    commentForm = CommentModelForm()
    return render(request,'posts/list.html', {'posts' : posts, 'commentForm':commentForm})
    
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

@login_required
def like(request, post_id):
    #like를 추가할 post를 가져옴
    post = get_object_or_404(Post,pk=post_id)
    # 만약 user가 해당 포스트를 이미 like했다면 like를 제거하고
    if request.user in post.like_users.all() :
        post.like_users.remove(request.user)
    else :
        post.like_users.add(request.user)
    
    return redirect('posts:list')
        
    # 아니라면, like를 추가한다.
    
    
@login_required
@require_POST
def create_comment(request, post_id):
    
    form = CommentModelForm(request.POST)
    if form.is_valid() :
        comment = form.save(commit=False)
        comment.post_id = post_id
        comment.user = request.user
        comment.save()
    
    return redirect('posts:list')

def delete_comment(request, comment_id) :
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    
    return redirect('posts:list')