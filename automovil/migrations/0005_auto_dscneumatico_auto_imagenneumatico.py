# Generated by Django 5.0.1 on 2024-03-08 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automovil', '0004_auto_dscauto'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='dscNeumatico',
            field=models.CharField(default='Valor predeterminado', max_length=500),
        ),
        migrations.AddField(
            model_name='auto',
            name='imagenNeumatico',
            field=models.ImageField(blank=True, null=True, upload_to='auto'),
        ),
    ]