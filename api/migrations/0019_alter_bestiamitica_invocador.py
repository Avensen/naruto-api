# Generated by Django 3.2.13 on 2022-06-13 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_alter_bestiamitica_invocador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bestiamitica',
            name='invocador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ninja'),
        ),
    ]