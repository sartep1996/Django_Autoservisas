# Generated by Django 4.2.1 on 2023-05-31 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automobiliomodelis',
            name='marke',
            field=models.CharField(help_text='Iveskite automobilio marke (pvz. ford)', max_length=100, verbose_name='Markė'),
        ),
    ]
