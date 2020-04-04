# Generated by Django 3.0.5 on 2020-04-03 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200404_0118'),
        ('childs', '0002_auto_20200404_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='course',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='childs', to='blog.Course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='child',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='name',
            field=models.CharField(db_index=True, max_length=40, verbose_name='Имя ученика'),
        ),
    ]
