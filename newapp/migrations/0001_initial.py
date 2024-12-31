# Generated by Django 5.0.7 on 2024-07-28 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emergencies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('hospital', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('blood', models.CharField(choices=[('B+', 'B+'), ('A+', 'A+'), ('A', 'A'), ('B', 'B'), ('O', 'O'), ('O+', 'O+'), ('AB', 'AB'), ('AB+', 'AB+')], max_length=10)),
                ('reason', models.CharField(max_length=200)),
            ],
        ),
    ]