# Generated by Django 2.2.5 on 2019-11-28 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlblog', '0008_auto_20191128_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_main_image',
            field=models.FileField(upload_to='blog/images/'),
        ),
        migrations.AlterField(
            model_name='usecase',
            name='usecase_main_image',
            field=models.FileField(upload_to='usecase/images/'),
        ),
    ]