# Generated by Django 3.2 on 2022-03-27 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='create',
            new_name='created',
        ),
    ]
