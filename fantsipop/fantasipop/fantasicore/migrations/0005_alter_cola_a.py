# Generated by Django 3.2.8 on 2021-11-03 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantasicore', '0004_cola_a'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cola',
            name='a',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
