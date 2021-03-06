# Generated by Django 3.2.13 on 2022-06-12 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_bestiamitica'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('ninja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resto_equipo_excluyendo_ninja_1', to='api.ninja')),
                ('ninja2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resto_equipo_excluyendo_ninja_2', to='api.ninja')),
                ('ninjamedico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resto_equipo_excluyendo_ninja_medico', to='api.ninjamedico')),
            ],
        ),
        migrations.CreateModel(
            name='Mision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=50)),
                ('pais_cliente', models.CharField(max_length=30)),
                ('rango', models.CharField(max_length=1)),
                ('recompensa', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='ninjatecnica',
            name='id_ninja',
        ),
        migrations.RemoveField(
            model_name='ninjatecnica',
            name='id_tecnica',
        ),
        migrations.AddField(
            model_name='ninjatecnica',
            name='ninja',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tecnicas', to='api.ninja'),
        ),
        migrations.AddField(
            model_name='ninjatecnica',
            name='tecnica',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ninjas', to='api.tecnica'),
        ),
        migrations.CreateModel(
            name='Pergamino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_sellado', models.DateField()),
                ('id_ninja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ninja')),
                ('id_tecnica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tecnica')),
            ],
        ),
        migrations.CreateModel(
            name='EquipoEnMision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('resultado', models.CharField(choices=[('S', 'Satisfactorio'), ('NS', 'No Satisfactorio')], max_length=20)),
                ('cantidad_shurikens', models.IntegerField()),
                ('cantidad_kunais', models.IntegerField()),
                ('cantidad_sellos', models.IntegerField()),
                ('capitan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.jounin')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='misiones', to='api.equipo')),
                ('mision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipos', to='api.mision')),
            ],
        ),
    ]
