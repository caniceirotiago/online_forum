from django import forms
from .models import Topic
from .models import Post

class NewTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title']
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']