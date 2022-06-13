# Generated by Django 3.2.13 on 2022-06-13 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20220613_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bestiamisionpergaminollave',
            name='bestia',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.bestiamitica'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='ninja1',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='exceptuar_ninja_1', serialize=False, to='api.ninja'),
        ),
        migrations.AlterField(
            model_name='equipoenmision',
            name='equipo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.equipo'),
        ),
        migrations.AlterField(
            model_name='equipoenmisionpergamino',
            name='equipoenmision',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.equipoenmision'),
        ),
        migrations.AlterField(
            model_name='ninjatecnica',
            name='ninja',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.ninja'),
        ),
    ]
