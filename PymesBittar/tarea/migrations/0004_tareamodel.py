# Generated by Django 4.0.6 on 2022-10-16 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarea', '0003_alter_tarea_fecha_entrega_alter_tarea_hora_entrega_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tareaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarea_fields', models.CharField(max_length=200)),
            ],
        ),
    ]
