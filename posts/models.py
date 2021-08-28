from django.db import models
from django.utils import timezone

# Create your models here.
CHOICES = (
    ("0","Linux"),
    ("1","Web"),
    ("2","Network"),
    ("3","programming"),
    ("4","PC操作"),
    ("5","その他") 
)
class Post(models.Model):
    day = models.DateField(verbose_name='日付', default=timezone.now)
    pulldown = models.CharField(verbose_name='ジャンル',choices=CHOICES,max_length=10)
    text = models.TextField(verbose_name='問題内容', max_length=200)
    answer = models.TextField(verbose_name='問題の答え', max_length=200)
    created_at = models.DateTimeField(verbose_name='通知日時', default=timezone.now)

    def __str__(self):
        return self.text