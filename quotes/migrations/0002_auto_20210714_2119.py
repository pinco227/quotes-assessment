# Generated by Django 3.2.5 on 2021-07-14 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='context',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='source',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
