# Generated by Django 3.2.8 on 2021-10-28 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fantasicore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='ticket',
        ),
    ]