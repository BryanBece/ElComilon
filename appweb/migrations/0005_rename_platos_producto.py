# Generated by Django 4.2.1 on 2023-06-21 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0004_alter_platos_imagen'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Platos',
            new_name='Producto',
        ),
    ]
