# Generated by Django 3.0.8 on 2020-07-08 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleTypeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(choices=[('car', 'car'), ('bike', 'bike')], max_length=100)),
                ('charge', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VehicleInformationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
                ('vehicle_number_plate', models.CharField(max_length=10)),
                ('brand', models.CharField(max_length=100)),
                ('vehicle_owner', models.CharField(max_length=100)),
                ('vehicle_owner_email', models.EmailField(max_length=100)),
                ('vehicle_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vehicle.VehicleTypeModel')),
            ],
        ),
    ]
