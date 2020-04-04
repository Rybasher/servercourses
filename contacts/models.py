from django.db import models

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя преподавателя', db_index=True)
    phone = models.CharField(max_length=50, verbose_name='Номер')
    telegram = models.CharField(max_length=50, verbose_name='Телеграм')
    email = models.EmailField(max_length=50, verbose_name='Эмайл')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'
        ordering = ['name']