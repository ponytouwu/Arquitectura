# Generated by Django 3.2.8 on 2021-11-03 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fantasicore', '0006_auto_20211103_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cola',
            name='atraccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fantasicore.atraccion'),
        ),
        migrations.AlterField(
            model_name='cola',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fantasicore.usuario'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fantasicore.usuario'),
        ),
        migrations.AlterField(
            model_name='tipo_atraccion',
            name='id_tipo_atr',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
