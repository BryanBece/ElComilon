# Generated by Django 4.2.2 on 2023-07-07 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0026_pedido_detallepedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='detallePedido',
        ),
    ]