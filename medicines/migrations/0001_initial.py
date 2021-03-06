# Generated by Django 3.0.8 on 2020-08-02 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('img_src', models.URLField(default='')),
                ('report_count', models.PositiveIntegerField(default=0)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicines.Medicine')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicines.Source')),
            ],
        ),
    ]
