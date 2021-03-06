from django.db import models
from django import forms
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.utils import timezone
# Create your models here.

#  tuple for STATUS of a post to keep draft and published posts separated when we render them out with templates.
STATUS = (
    (0,'Draft'),
    (1,'Publish')
);



class Blog(models.Model):
    blog_main_image = models.FileField(upload_to='blog/images/')
    title = models.CharField(max_length=200,null=True, blank=False)
    summary = models.CharField(max_length=200,null=True, blank=False)
    slug = models.SlugField(max_length=200,unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)

    content = RichTextUploadingField(config_name='special',external_plugin_resources=[
        ('youtube','/static/youtube/','plugin.js')])

    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS,default=0)

    # tell Django to sort results in the created_on field in descending order using the negative prefix
    class Meta:
        ordering = ['-created_on']

    # The __str__() method is the default human-readable representation of the object.
    # Django will use it in many places, such as the administration site.
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_home', kwargs={'slug': self.slug})


class UseCase(models.Model):
    usecase_main_image = models.FileField(upload_to='usecase/images/')
    usecase_title = models.CharField(max_length=50)
    usecase_summary = models.CharField(max_length=80)
    usecase_slug = models.SlugField(max_length=200)
    usecase_author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='usecase_posts')
    usecase_updated_on = models.DateTimeField(auto_now=True)
    usecase_content = models.TextField()
    usecase_created_on = models.DateTimeField(auto_now_add=True)
    usecase_status = models.IntegerField(choices=STATUS,default=0)

    # tell Django to sort results in the created_on field in descending order using the negative prefix
    class Meta:
        ordering = ['-usecase_created_on']

    # The __str__() method is the default human-readable representation of the object.
    # Django will use it in many places, such as the administration site.
    def __str__(self):
        return self.usecase_title


class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)


    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

