from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from .models import Post
def index(request):
    params = {
        'title':'ようこそ！想起アプリへ！',
        'msg':'早速問題を作りましょう！',
        'form': PostForm(),
        'result':None,
        'goto':'問題一覧',
    }
    
    if (request.method == 'POST'):
        ch = request.POST['choice']
        params['result'] = 'selected:"' + ch + '"'
        params['form'] = PostForm(request.POST)        
    return render(request,'posts/index.html',params)

def list(request):
    data = Post.objects.all()
    params = {
        'title':'問題一覧',
        'msg':'編集したい問題を選んでください',
        'data': data,
        'goto':'問題作成ページ',
    }
    return render(request,'posts/index.html',params)

#class PostCreateView(CreateView):
    template_name = 'index.html'
    form_class = PostForm


# Create your views here.
