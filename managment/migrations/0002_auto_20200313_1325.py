# Generated by Django 3.0.3 on 2020-03-13 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='Budget1',
            new_name='Budget',
        ),
    ]