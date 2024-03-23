from django.db import models

class PepperFormat(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    last_modified = models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')
    length = models.FloatField(verbose_name='Длина мм',default=None)
    width = models.FloatField(verbose_name='Ширина мм',default=None)

    class Meta:
        verbose_name = 'Формат бумаги'
        verbose_name_plural = 'Форматы бумаг'

    def __str__(self):
        return self.name







