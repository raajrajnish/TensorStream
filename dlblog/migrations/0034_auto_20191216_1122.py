# Generated by Django 2.2.8 on 2019-12-16 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlblog', '0033_auto_20191216_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='summary',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]