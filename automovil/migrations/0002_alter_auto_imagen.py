# Generated by Django 5.0.1 on 2024-03-06 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automovil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='auto'),
        ),
    ]
