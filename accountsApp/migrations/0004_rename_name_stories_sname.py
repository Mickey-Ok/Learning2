# Generated by Django 4.1.7 on 2023-04-11 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accountsApp', '0003_alter_genres_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stories',
            old_name='name',
            new_name='sname',
        ),
    ]
