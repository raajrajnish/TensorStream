# Generated by Django 2.2.5 on 2019-12-06 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlblog', '0015_blog1'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog1',
            name='blog_main_image',
            field=models.FileField(default=None, upload_to='images/'),
        ),
    ]
