from django.db.models import Model, CharField, ForeignKey, TextField, EmailField, DateTimeField
from django.contrib.auth.models import AbstractUser
from ckeditor_uploader.fields import RichTextUploadingField

class Account(AbstractUser):
    last_name = CharField(max_length=50, verbose_name='Фамилия', unique=True)
    username = CharField(max_length=50, verbose_name='Имя')
    cabinet = CharField(max_length=5, verbose_name='Кабинет')
    email = EmailField(max_length=254, verbose_name='Адрес электронной почты')
    USERNAME_FIELD = 'last_name'
    REQUIRED_FIELDS = ('username', 'email')

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return (
            str(self.last_name) + " " + str(self.username) + " " + str(self.email)
        )

class Ticket(Model):
    TODAY = 'Сегодня'
    WEEK = 'Неделя'
    MOUNTH = 'Месяц'
    YEAR = 'Год (на оборудование)'
    PRIORITY = (
        (TODAY, 'Сегодня'),
        (WEEK, 'Неделя'),
        (MOUNTH, 'Месяц'),
        (YEAR, 'Год (на оборудование)')
    )
    priority = CharField(max_length=50, choices = PRIORITY, verbose_name='Приоритет')
    text = TextField(verbose_name='сообщение')
    published = DateTimeField(auto_now_add=True)
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
    status = CharField(max_length=50, choices = STATUS, default=REGISTER, verbose_name='Статус')

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return (
            str(self.published.strftime('%d.%m.%Y %H:%M')) + 
            " " + str(self.priority) + " " + str(self.status)
        )

class Tutorial(Model):
    title = CharField("Заголовок", max_length = 100)
    content = RichTextUploadingField("Решение")
    def __str__(self):
        return str(self.title)
    class Meta:
        verbose_name_plural = "база знаний"
        verbose_name = "база знаний"
