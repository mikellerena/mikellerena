# Generated by Django 3.0.4 on 2020-04-20 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appProduccion', '0003_auto_20200411_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('codigo', models.CharField(max_length=75, primary_key=True, serialize=False)),
                ('cliente', models.CharField(max_length=50)),
                ('fecha_inicio', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='proceso',
            name='codigo_orden_fabricacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appProduccion.Orden'),
        ),
    ]
