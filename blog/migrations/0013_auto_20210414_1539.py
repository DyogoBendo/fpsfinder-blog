# Generated by Django 3.2 on 2021-04-14 18:39

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_post_slang'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='font_banner',
            field=models.URLField(default='empty'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postfile',
            name='file',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
