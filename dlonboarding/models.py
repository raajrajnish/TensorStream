from django.db import models

# Create your models here.

class UserInfo(models.Model):

    username = models.CharField(max_length=120,unique=False)
    unique_username = models.CharField(max_length=120,unique=True)
    email = models.CharField(max_length=120,unique=True)
    password = models.CharField(max_length=120)
    confirm_password = models.CharField(max_length=120)
    created_on = models.DateTimeField(auto_now_add=True)

    # tell Django to sort results in the created_on field in descending order using the negative prefix
    class Meta:
        ordering = ['-created_on']

