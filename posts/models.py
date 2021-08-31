from django.db import models
from django.utils import timezone

# Create your models here.
CHOICES = (
    ("Linux","Linux"),#左はHTMLにデータとして表示させる値、右はプルダウンで表示させる値
    ("Web","Web"),
    ("Network","Network"),
    ("プログラミング","Programming"),
    ("PC操作","PC操作"),
    ("その他","その他") 
)

class Post(models.Model):
    day = models.DateField(verbose_name='日付', default=timezone.now)
    pulldown = models.CharField(verbose_name='ジャンル',choices=CHOICES,max_length=10)
    text = models.TextField(verbose_name='問題内容', max_length=200)
    answer = models.TextField(verbose_name='問題の答え', max_length=200)
    created_at = models.DateTimeField(verbose_name='通知日時', default=timezone.now)
    reference = models.URLField(verbose_name='参考URL', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.text