# Generated by Django 3.2.5 on 2021-07-14 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_auto_20210714_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='context',
            field=models.CharField(blank=True, default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quote',
            name='source',
            field=models.CharField(blank=True, default=None, max_length=100),
            preserve_default=False,
        ),
    ]
