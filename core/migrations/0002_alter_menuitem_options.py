# Generated by Django 4.2 on 2023-04-25 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menuitem',
            options={'verbose_name': 'Пункт меню', 'verbose_name_plural': 'Пункты меню'},
        ),
    ]
