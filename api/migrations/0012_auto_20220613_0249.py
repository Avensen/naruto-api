# Generated by Django 3.2.13 on 2022-06-13 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20220613_0246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pergamino',
            old_name='id_ninja',
            new_name='ninja',
        ),
        migrations.RenameField(
            model_name='pergamino',
            old_name='id_tecnica',
            new_name='tecnica',
        ),
        migrations.AlterField(
            model_name='equipoenmision',
            name='equipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.equipo'),
        ),
        migrations.AlterField(
            model_name='equipoenmision',
            name='mision',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mision'),
        ),
        migrations.AlterUniqueTogether(
            name='equipoenmision',
            unique_together={('equipo', 'mision')},
        ),
    ]