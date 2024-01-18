from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    message = models.TextField(verbose_name='Сообщение')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_accept = models.BooleanField(default=False, verbose_name='Принята')
    date_accept = models.DateTimeField(auto_now=True, verbose_name='Дата принятия')

    class Meta:
        verbose_name = 'заявку'
        verbose_name_plural = 'заявки'

    def __str__(self):
        return f'{self.name} {self.phone}'

