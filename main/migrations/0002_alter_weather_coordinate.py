# Generated by Django 5.0.2 on 2024-02-26 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='coordinate',
            field=models.CharField(max_length=10),
        ),
    ]
