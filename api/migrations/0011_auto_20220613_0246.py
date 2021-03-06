# Generated by Django 3.2.13 on 2022-06-13 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_bestiamisionpergaminollave_equipoenmisionpergamino'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bestiamisionpergaminollave',
            old_name='id_bestia',
            new_name='bestia',
        ),
        migrations.RenameField(
            model_name='bestiamisionpergaminollave',
            old_name='id_mision',
            new_name='mision',
        ),
        migrations.RenameField(
            model_name='bestiamisionpergaminollave',
            old_name='id_pergamino',
            new_name='pergamino',
        ),
        migrations.AlterUniqueTogether(
            name='bestiamisionpergaminollave',
            unique_together={('bestia', 'mision', 'pergamino')},
        ),
    ]
