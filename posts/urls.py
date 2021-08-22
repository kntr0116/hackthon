from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('', views.index, name='問題作成ページ'),
    path('list', views.list, name='問題一覧')
    ]