# Generated by Django 3.2.7 on 2021-11-25 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(verbose_name='Expenses date'),
        ),
    ]
