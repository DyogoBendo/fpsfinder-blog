# Generated by Django 3.2 on 2021-04-13 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_banner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='banner',
        ),
        migrations.RemoveField(
            model_name='post',
            name='banner_url',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='published',
        ),
    ]