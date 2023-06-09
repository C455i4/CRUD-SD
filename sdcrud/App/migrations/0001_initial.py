# Generated by Django 4.2 on 2023-04-21 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo_acao', models.CharField(max_length=10)),
                ('descricao', models.TextField(max_length=200)),
                ('data', models.DateField()),
                ('open', models.FloatField()),
                ('close', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('volume', models.IntegerField(default='0')),
            ],
        ),
    ]
