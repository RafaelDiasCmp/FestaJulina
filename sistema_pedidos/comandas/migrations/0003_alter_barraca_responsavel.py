# Generated by Django 5.0.6 on 2024-05-09 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comandas', '0002_barraca_responsavel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barraca',
            name='responsavel',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
