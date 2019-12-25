from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

STATUS = (
    (0,'Draft'),
    (1,'Publish')
)

class offerings(models.Model):
    course_main_image = models.FileField(upload_to='blog/images/')
    course_title = models.CharField(max_length=200,null=True, blank=False)
    course_name = models.CharField(max_length=200,null=True, blank=False)
    course_slug = models.SlugField(max_length=200,unique=True)
    course_created_on = models.DateTimeField(auto_now_add=True)
    course_status = models.IntegerField(choices=STATUS, default=0)
    course_author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='course_post')

    class Meta:
        ordering = ['-course_created_on']

    # The __str__() method is the default human-readable representation of the object.
    # Django will use it in many places, such as the administration site.
    def __str__(self):
        return self.course_title

    def get_absolute_url(self):
        return reverse('blog_home', kwargs={'slug': self.course_slug})

