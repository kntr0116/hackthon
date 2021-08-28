from django import forms
from.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['day','pulldown','text','answer','created_at']
    #data=[
        #('one', 'Linux'),
        #('two', 'web'),
        #('three', 'Network'),
        #('four', 'programming'),
        #('five', 'PC操作'),
        #('six', 'その他'),
    #]
    #choice = forms.ChoiceField(label='ジャンル',choices=data , widget=forms.TextInput(attrs={'class':'form-control','size': 1}))
    #text = forms.CharField(label='問題内容',widget=forms.TextInput(attrs={'class':'form-control'}))
    #answer = forms.CharField(label='問題の答え',widget=forms.TextInput({'class':'form-control'}))
    #time = forms.DateTimeField(label='通知する日時',widget=forms.DateInput({'class':'form-control'}))

