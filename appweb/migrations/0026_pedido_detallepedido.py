# Generated by Django 4.2.2 on 2023-07-07 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0025_alter_pedido_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='detallePedido',
            field=models.TextField(blank=True, null=True),
        ),
    ]
