# Generated by Django 3.2.13 on 2022-06-13 09:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_persona_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chunin',
            name='calificacion_examen',
            field=models.DateField(default=datetime.date(1, 1, 1)),
        ),
        migrations.AlterField(
            model_name='chunin',
            name='fecha_examen',
            field=models.DateField(default=datetime.date(1, 1, 1)),
        ),
        migrations.AlterField(
            model_name='equipoenmision',
            name='fecha_fin',
            field=models.DateField(default=datetime.date(1, 1, 1)),
        ),
        migrations.AlterField(
            model_name='equipoenmision',
            name='fecha_inicio',
            field=models.DateField(default=datetime.date(1, 1, 1)),
        ),
        migrations.AlterField(
            model_name='genin',
            name='fecha_graduacion',
            field=models.DateField(default=datetime.date(1, 1, 1)),
        ),
        migrations.AlterField(
            model_name='jounin',
            name='calificacion_examen',
            field=models.DateField(default=datetime.date(1, 1, 1)),
        ),
        migrations.AlterField(
            model_name='jounin',
            name='fecha_examen',
            field=models.DateField(default=datetime.date(1, 1, 1)),
        ),
        migrations.AlterField(
            model_name='pergamino',
            name='fecha_sellado',
            field=models.DateField(default=datetime.date(1, 1, 1)),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.date(1, 1, 1)),
        ),
    ]
