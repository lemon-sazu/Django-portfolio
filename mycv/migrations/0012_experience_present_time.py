# Generated by Django 3.0.8 on 2020-08-10 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycv', '0011_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='present_time',
            field=models.CharField(blank=True, default='Present', max_length=50),
        ),
    ]