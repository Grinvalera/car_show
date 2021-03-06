# Generated by Django 3.1.7 on 2021-03-24 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=256, verbose_name='Марка')),
                ('model', models.CharField(max_length=256, verbose_name='Модель')),
                ('body_type', models.CharField(max_length=256, verbose_name='Тип кузова')),
                ('year_issue', models.IntegerField(verbose_name='Год выпуска')),
                ('mileage', models.IntegerField(blank=True, null=True, verbose_name='Пробег')),
                ('city', models.CharField(max_length=256, verbose_name='Город')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('transmission', models.CharField(max_length=128, verbose_name='Коробка передач')),
                ('fuel', models.CharField(max_length=128, verbose_name='Тип топлива')),
                ('drive_unit', models.CharField(max_length=128, verbose_name='Тип привода')),
                ('engine_capacity', models.CharField(max_length=128, verbose_name='Объем двигателя')),
                ('engine_power', models.IntegerField(verbose_name='Мощность двигателя')),
                ('color_car', models.CharField(max_length=128, verbose_name='Цвет авто')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена авто ')),
            ],
            options={
                'verbose_name': 'Авто',
                'verbose_name_plural': 'Автомобили',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=256, verbose_name='Фамилия')),
                ('third_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Отчество')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('phone_number', models.CharField(max_length=256, verbose_name='Номер телефона')),
                ('city', models.CharField(max_length=256, verbose_name='Город проживания')),
                ('_password', models.CharField(max_length=128, verbose_name='Пароль')),
                ('_remember_password', models.CharField(max_length=128, verbose_name='Повторный пароль')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='car_images')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.user'),
        ),
    ]
