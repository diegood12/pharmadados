# Generated by Django 3.0.8 on 2020-08-02 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0002_auto_20200802_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='type',
            field=models.SmallIntegerField(choices=[(0, 'News'), (1, 'Article')]),
        ),
    ]
