# Generated by Django 2.2.1 on 2019-05-23 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0003_auto_20190523_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='completion_date',
            field=models.DateTimeField(verbose_name='Срок исполнения заявки'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='published_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='published_time',
            field=models.TimeField(),
        ),
    ]