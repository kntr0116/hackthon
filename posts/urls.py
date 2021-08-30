from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('', views.index, name='問題一覧ページ'),
    path('<int:num>', views.index, name='問題一覧ページ'),
    path('create', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
    path('tyousen/<int:num>', views.tyousen, name='tyousen'),# 問題に回答するページに遷移。views.pyのtyousenメソッドを呼び出し。
    ]