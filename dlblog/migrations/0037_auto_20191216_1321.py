# Generated by Django 2.2.8 on 2019-12-16 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlblog', '0036_auto_20191216_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='summary',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
