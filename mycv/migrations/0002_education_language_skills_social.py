# Generated by Django 3.0.8 on 2020-08-09 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inc_name', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=50)),
                ('board', models.CharField(max_length=50)),
                ('group', models.CharField(max_length=50)),
                ('start_yer', models.DateField()),
                ('end_yer', models.DateField()),
                ('passing_yer', models.DateField()),
                ('results', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='skills/')),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_name', models.CharField(max_length=50)),
                ('urls', models.URLField()),
            ],
        ),
    ]