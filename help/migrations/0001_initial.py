# Generated by Django 2.2.1 on 2019-07-07 14:33

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('last_name', models.CharField(max_length=50, unique=True, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Адрес электронной почты')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Администратор')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Учетная запись',
                'verbose_name_plural': 'Учетные записи',
            },
        ),
        migrations.CreateModel(
            name='Manual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Решение')),
            ],
            options={
                'verbose_name': 'Руководство пользователя',
                'verbose_name_plural': 'Руководства пользователя',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabinet', models.CharField(max_length=50, verbose_name='Кабинет')),
                ('priority', models.CharField(choices=[('День', 'День'), ('Неделя', 'Неделя'), ('Месяц', 'Месяц'), ('Год (на оборудование)', 'Год (на оборудование)')], max_length=50, verbose_name='Приоритет')),
                ('text', models.TextField(verbose_name='сообщение')),
                ('published_date', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
                ('published_time', models.TimeField(auto_now_add=True, verbose_name='Время публикации')),
                ('comment', models.CharField(blank=True, max_length=200, null=True, verbose_name='Комментарий')),
                ('completion_date', models.DateTimeField(blank=True, null=True, verbose_name='Срок исполнения заявки')),
                ('status', models.CharField(choices=[('Зарегистрирована', 'Зарегистрирована'), ('Исполняется', 'Исполняется'), ('Отменена', 'Отменена'), ('Исполнена', 'Исполнена')], default='Зарегистрирована', max_length=50, verbose_name='Статус')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
