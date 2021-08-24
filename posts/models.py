from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    day = models.DateField(verbose_name='日付', default=timezone.now)
    choice = models.CharField(verbose_name='ジャンル',max_length=20)
    text = models.TextField(verbose_name='問題内容', max_length=200)
    answer = models.TextField(verbose_name='問題の答え', max_length=200)
    #created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)

    def __str__(self):
        return self.choice  