# Generated by Django 3.0.8 on 2020-08-02 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0003_auto_20200802_1836'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='img_src',
            new_name='Image Source',
        ),
    ]
