# Generated by Django 5.0.7 on 2024-10-07 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_delete_counters_emergencies_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='emergencies',
            name='photo',
            field=models.ImageField(blank=True, default='patient.webp', upload_to=''),
        ),
    ]