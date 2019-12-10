from django.forms import ModelForm
from .models import Blog



class addMainContent(ModelForm):

    class Meta:
        model = Blog
        fields = ('blog_main_image', 'title', 'summary', 'content')

