from django.forms import ModelForm
from .models import Blog,Comment



class addMainContent(ModelForm):

    class Meta:
        model = Blog
        fields = ('blog_main_image', 'title', 'summary', 'content')


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')