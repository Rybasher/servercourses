from django.db import models
from django.utils.text import slugify
# Create your models here.
from time import time


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + "-" + str(int(time()))


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название поста')
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    image = models.ImageField(verbose_name='Фото продукта', height_field="height_field",
                              width_field="width_field", upload_to=upload_location)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    link = models.CharField(max_length=300, verbose_name='Ссылка на видео')
    published_date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    homework = models.TextField(verbose_name='Домашнее задание')
    views = models.IntegerField('Просмотры', default=0)
    course = models.ForeignKey('Course', related_name='posts', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return "post/%s" % self.slug

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['-published_date']


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название курса')
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def get_absolute_url(self):
        return "course/%s" % self.slug

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

