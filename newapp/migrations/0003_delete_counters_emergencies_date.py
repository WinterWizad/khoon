# Generated by Django 5.0.7 on 2024-10-07 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_counters'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Counters',
        ),
        migrations.AddField(
            model_name='emergencies',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
