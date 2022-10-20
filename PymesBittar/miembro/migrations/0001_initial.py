# Generated by Django 4.0.6 on 2022-10-11 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='miembro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(blank=True, max_length=250, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=250, null=True)),
                ('nacionalidad', models.CharField(blank=True, max_length=250, null=True)),
                ('numero_de_documento', models.CharField(blank=True, max_length=250, null=True)),
                ('fecha_de_nacimiento', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono_particular', models.CharField(blank=True, max_length=250, null=True)),
                ('telefono_corporativo', models.CharField(blank=True, max_length=250, null=True)),
                ('mail_particular', models.CharField(blank=True, max_length=250, null=True)),
                ('mail_corporativo', models.CharField(blank=True, max_length=250, null=True)),
                ('fecha_de_ingreso', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_de_salida', models.CharField(blank=True, max_length=50, null=True)),
                ('motivo_de_salida', models.CharField(blank=True, max_length=250, null=True)),
                ('cargo', models.CharField(blank=True, max_length=250, null=True)),
                ('notas_adicionales', models.CharField(blank=True, max_length=250, null=True)),
                ('contribuyente_set', models.CharField(choices=[('1', 'Si'), ('2', 'No')], max_length=20)),
                ('estado_civil', models.CharField(choices=[('1', 'Soltero'), ('2', 'Casado'), ('3', 'Viudo'), ('4', 'Divorciado')], max_length=250)),
                ('hijos', models.CharField(choices=[('1', 'Si'), ('2', 'No')], max_length=250)),
                ('genero', models.CharField(choices=[('1', 'Efectivo'), ('H', 'Hombre'), ('M', 'Mujer'), ('PNM', 'Prefiero no mencionarlo')], max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
