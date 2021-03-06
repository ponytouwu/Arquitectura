# Generated by Django 3.2.8 on 2021-11-03 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fantasicore', '0002_remove_usuario_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='usuario',
            field=models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, to='fantasicore.usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='appellidos_us',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fono_us',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
