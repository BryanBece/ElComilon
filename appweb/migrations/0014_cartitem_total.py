# Generated by Django 4.2.2 on 2023-06-27 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0013_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='total',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
