# Generated by Django 2.1.5 on 2019-01-10 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_number', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('user_email', models.EmailField(max_length=50)),
                ('car_model', models.CharField(max_length=50)),
                ('car_seats', models.IntegerField()),
                ('car_source', models.CharField(max_length=50)),
                ('car_destination', models.CharField(max_length=50)),
                ('car_depttime', models.CharField(max_length=50)),
                ('car_retntime', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'user_car',
            },
        ),
    ]