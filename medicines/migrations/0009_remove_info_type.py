# Generated by Django 3.0.8 on 2020-08-07 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0008_auto_20200803_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='type',
        ),
    ]
