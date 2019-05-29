from django.db.models import Model, CharField, ForeignKey, TextField, EmailField, DateField, DateTimeField, TimeField
from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Account(AbstractUser):
    username = CharField(max_length=50, verbose_name='Фамилия', unique=True)
    first_name = CharField(max_length=50, verbose_name='Имя')
    email = EmailField(max_length=254, verbose_name='Адрес электронной почты')
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('first_name', 'email')

    class Meta:
        verbose_name = "Учетная запись"
        verbose_name_plural = "Учетные записи"

    def __str__(self):
        return (
            str(self.username) + " " + str(self.first_name) + " " + str(self.email)
        )

class Ticket(Model):
    client = ForeignKey(Account, on_delete=models.CASCADE, null=True, verbose_name='Клиент')
    cabinet = CharField(max_length=50, verbose_name='Кабинет')
    DAY = 'День'
    WEEK = 'Неделя'
    MOUNTH = 'Месяц'
    YEAR = 'Год (на оборудование)'
    PRIORITY = (
        (DAY, 'День'),
        (WEEK, 'Неделя'),
        (MOUNTH, 'Месяц'),
        (YEAR, 'Год (на оборудование)')
    )
    priority = CharField(max_length=50, choices = PRIORITY, verbose_name='Приоритет')
    text = TextField(verbose_name='сообщение')
    published_date = DateField(auto_now_add=True, verbose_name='Дата публикации')
    published_time = TimeField(auto_now_add=True, verbose_name='Время публикации')
    REGISTER = 'Зарегистрирована'
    PERFORMED = 'Исполняется'
    CANCEL = 'Отменена'
    DONE = 'Исполнена'
    STATUS = (
        (REGISTER, 'Зарегистрирована'),
        (PERFORMED, 'Исполняется'),
        (CANCEL, 'Отменена'),
        (DONE, 'Исполнена')
    )
    completion_date = DateTimeField(verbose_name='Срок исполнения заявки', null=True)
    status = CharField(max_length=50, choices = STATUS, default=REGISTER, verbose_name='Статус')

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return (
            str(self.published_date.strftime('%d.%m.%Y')) +
            " " + str(self.published_time.strftime('%H:%M')) +
            " " + str(self.priority) + " " + str(self.status)
        )

class Manual(Model):
    title = CharField("Заголовок", max_length = 100)
    content = RichTextUploadingField("Решение")
    def __str__(self):
        return str(self.title)
    class Meta:
        verbose_name = "Руководство пользователя"
        verbose_name_plural = "Руководства пользователя"

def user_full_name(self):
    return '%s %s' % (self.username, self.first_name)

Account.__str__ = user_full_name
