# Generated by Django 5.0.6 on 2024-07-14 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_car_date_of_birth_remove_car_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]