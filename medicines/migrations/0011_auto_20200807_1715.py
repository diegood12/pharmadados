# Generated by Django 3.0.8 on 2020-08-07 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0010_medicine_en_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='en_name',
            field=models.CharField(max_length=50, verbose_name='English name'),
        ),
    ]
