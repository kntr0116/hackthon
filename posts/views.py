from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from .models import Post
from django.shortcuts import redirect
from django.core.paginator import Paginator

def index(request,num=1):
    data = Post.objects.all()
    page = Paginator(data, 3)
    params = {
        'data': page.get_page(num)
    }
    return render(request, 'posts/index.html', params)

def create(request):
    if (request.method == 'POST'):
        obj = Post()
        post = PostForm(request.POST, instance=obj)
        post.save()
        return redirect(to='/posts')
    params = {
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
