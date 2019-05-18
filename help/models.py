from django.db.models import Model, CharField, ForeignKey, TextField, EmailField, DateTimeField
from django.contrib.auth.models import AbstractUser

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
            str(self.last_name) + " " + str(self.first_name) + " " + str(self.email)
        )

class Ticket(Model):
    REPAIR = 'Ремонт и замена техники'
    SOFTWARE_UPDATE = 'Обновление программного обеспечения'
    HELP = 'Помощь с программным обеспечением'
    TROUBLESHOOTING = 'Устранение проблем с программным обеспечением'
    REPLACEMENT = 'Замена периферийных устройств'
    TICKET_TYPE = (
        (REPAIR, 'Ремонт и замена техники'),
        (SOFTWARE_UPDATE, 'Обновление программного обеспечения'),
        (HELP, 'Помощь с программным обеспечением'),
        (TROUBLESHOOTING, 'Устранение проблем с программным обеспечением'),
        (REPLACEMENT, 'Замена периферийных устройств')
    )
    ticket_type = CharField(max_length=50, choices = TICKET_TYPE, verbose_name='Тип обращения')
    text = TextField(verbose_name='сообщение')
    published = DateTimeField(auto_now_add=True)
    QUEUE = 'В очереди'
    PERFORMED = 'Исполняется'
    DONE = 'Исполнено'
    STATUS = (
        (QUEUE, 'В очереди'),
        (PERFORMED, 'Исполняется'),
        (DONE, 'Исполнено')
    )
    status = CharField(max_length=50, choices = STATUS, verbose_name='Статус')

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return (
            str(self.published) + " " + str(self.ticket_type) + " " + str(self.status)
        )
