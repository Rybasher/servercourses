from django.db import models
from blog.models import Course
# Create your models here.
from django.utils.text import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + "-" + str(int(time()))


class Child(models.Model):
    name = models.CharField(max_length=40, verbose_name='Имя ученика', db_index=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    paid = models.BooleanField(default=False)
    homework = models.BooleanField(default=False)
    course = models.ForeignKey(Course, related_name='childs', on_delete=models.PROTECT)


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Ученики'
        verbose_name = "Ученик"
        ordering = ['pk']

