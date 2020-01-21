from django.forms import ModelForm
from .models import Topic
from django import forms

class TopicCreateForm(ModelForm):
    class Meta:
        model = Topic
        fields = [
            "title",
            "user_name",
            "category",
            "message",
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'hoge'}),
            'user_name': forms.TextInput(attrs={'value': '名無し'}),
            }

    def __init__(self, *args, **kwargs):
        # kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = '選択して下さい'
        self.fields['user_name'].widget.attrs['value'] = '匿名'
        # self.fields['title'].widget.attrs['class'] = 'huga'

