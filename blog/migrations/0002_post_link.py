# Generated by Django 3.0.5 on 2020-04-03 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.CharField(default='', max_length=300, verbose_name='Ссылка на видео'),
            preserve_default=False,
        ),
    ]
