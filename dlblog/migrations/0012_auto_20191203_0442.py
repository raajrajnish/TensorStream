# Generated by Django 2.2.5 on 2019-12-03 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlblog', '0011_auto_20191128_0513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]