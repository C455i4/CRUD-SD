# Generated by Django 4.2 on 2023-05-06 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_acao_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acao',
            name='close',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='acao',
            name='high',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='acao',
            name='low',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='acao',
            name='open',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='acao',
            name='volume',
            field=models.IntegerField(default=0),
        ),
    ]
