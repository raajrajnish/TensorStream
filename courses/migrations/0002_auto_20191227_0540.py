# Generated by Django 2.2.5 on 2019-12-27 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offerings',
            old_name='course_slug',
            new_name='slug',
        ),
    ]
