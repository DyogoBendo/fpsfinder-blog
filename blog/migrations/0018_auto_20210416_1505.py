# Generated by Django 3.2 on 2021-04-16 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='font_banner',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
