from django import forms

class PostForm(forms.Form):
    data=[
        ('one', 'Linux'),
        ('two', 'web'),
        ('three', 'Network'),
        ('four', 'programming'),
        ('five', 'PC操作'),
        ('six', 'その他'),
    ]
    choice = forms.ChoiceField(label='ジャンル',choices=data , widget=forms.Select(attrs={'size': 1}))
    text = forms.CharField(label='問題内容',widget=forms.Textarea)
    answer = forms.CharField(label='問題の答え',widget=forms.Textarea)
    time = forms.DateTimeField(label='通知する日時')

