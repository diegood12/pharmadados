# Generated by Django 3.1 on 2020-08-08 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0011_auto_20200807_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='title',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
