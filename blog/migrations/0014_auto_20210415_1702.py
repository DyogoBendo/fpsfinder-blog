# Generated by Django 3.2 on 2021-04-15 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20210414_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='banner_link',
            field=models.URLField(default='empty'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='font_banner',
            field=models.CharField(max_length=30),
        ),
    ]
