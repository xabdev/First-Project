# Generated by Django 2.2.24 on 2021-10-20 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]