# Generated by Django 5.0.6 on 2024-07-14 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='body_type',
            field=models.CharField(blank=True, choices=[('sedan', 'Седан'), ('hatchback', 'Хэтчбек'), ('SUV', 'Внедорожник'), ('wagon', 'Универсал'), ('minivan', 'Минивэн'), ('pickup', 'Пикап'), ('coupe', 'Купе'), ('cabrio', 'Кабриолет')]),
        ),
        migrations.AddField(
            model_name='car',
            name='drive_unit',
            field=models.CharField(blank=True, choices=[('rear', 'Задний'), ('front', 'Передний'), ('full', 'Полный')]),
        ),
        migrations.AddField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(blank=True, choices=[('gasoline', 'Бензин'), ('diesel', 'Дизель'), ('hybrid', 'Гибрид'), ('electro', 'Электро')]),
        ),
        migrations.AddField(
            model_name='car',
            name='gearbox',
            field=models.CharField(blank=True, choices=[('manual', 'Механика'), ('automatic', 'Автомат'), ('вариатор', 'CVT'), ('robot', 'Робот')]),
        ),
        migrations.AlterField(
            model_name='sale',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
