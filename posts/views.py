from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from .models import Post
from django.shortcuts import redirect

def index(request):
    data = Post.objects.all()
    params = {
        'title':'welcome！',
        'msg':'問題一覧',
        'data': data,
    }
    return render(request, 'posts/index.html', params)

def create(request):
    if (request.method == 'POST'):
        obj = Post()
        post = PostForm(request.POST, instance=obj)
        post.save()
        return redirect(to='/posts')
    params = {
        'title':'welcome！',
        'msg':'早速問題を作りましょう！',
        'form': PostForm(),    
    }       
    return render(request,'posts/create.html',params)

def edit(request, num):
    obj = Post.objects.get(id=num)
    if(request.method == 'POST'):
        post = PostForm(request.POST, instance=obj)
        post.save()
        return redirect(to='/posts')
    params = {
        'title':'welcome！',
        'msg':'問題を編集',
        'id':num,
        'form': PostForm(instance=obj), 
    }
    return render(request, 'posts/edit.html', params)

def delete(request, num):
    post = Post.objects.get(id=num)
    if(request.method == 'POST'):
        post.delete()
        return redirect(to='/posts')
    params = {
        'title':'welcome!!',
        'msg':'問題を削除',
        'id':num,
        'obj': post,
    }
    return render(request, 'posts/delete.html', params)
#class PostCreateView(CreateView):
    template_name = 'index.html'
    form_class = PostForm


# Create your views here.
