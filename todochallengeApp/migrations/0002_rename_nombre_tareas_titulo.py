# Generated by Django 4.1.3 on 2025-03-01 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todochallengeApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tareas',
            old_name='nombre',
            new_name='titulo',
        ),
    ]
