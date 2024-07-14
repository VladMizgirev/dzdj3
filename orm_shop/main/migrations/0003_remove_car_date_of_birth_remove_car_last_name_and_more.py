# Generated by Django 5.0.6 on 2024-07-14 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_car_id_alter_car_mileage_alter_car_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='car',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='car',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='car',
            name='name',
        ),
        migrations.RemoveField(
            model_name='car',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
    ]
