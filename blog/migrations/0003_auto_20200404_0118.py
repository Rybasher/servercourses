# Generated by Django 3.0.5 on 2020-04-03 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-published_date'], 'verbose_name': 'Урок', 'verbose_name_plural': 'Уроки'},
        ),
    ]