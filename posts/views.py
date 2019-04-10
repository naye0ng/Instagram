from django.shortcuts import render, redirect
from .forms import PostModelForm

# Create your views here.
def create(request):
    if request.method == "POST" :
        # 작성된 post를 DB에 적용
        form = PostModelForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('post:create')
    else :
        # post를 작성하는 form을 보여 줌
        form = PostModelForm()
        return render(request, 'posts/create.html', {'form': form})

