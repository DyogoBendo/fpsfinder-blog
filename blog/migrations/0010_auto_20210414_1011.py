# Generated by Django 3.2 on 2021-04-14 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210413_1546'),
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
            model_name='postfile',
            name='code',
        ),
        migrations.RemoveField(
            model_name='postfile',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='postfile',
            name='post',
        ),
        migrations.RemoveField(
            model_name='postfile',
            name='url',
        ),
        migrations.AlterField(
            model_name='postfile',
            name='file',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
    ]
