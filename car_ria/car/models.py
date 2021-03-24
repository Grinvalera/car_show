from django.db import models


class User(models.Model):
    """Модель пользователя сайта"""
    first_name = models.CharField(max_length=256, blank=False, null=False, verbose_name="Имя")
    last_name = models.CharField(max_length=256, blank=False, null=False, verbose_name="Фамилия")
    third_name = models.CharField(max_length=256, blank=True, null=True, verbose_name="Отчество")
    email = models.EmailField(blank=False, null=False, verbose_name="Электронная почта")
    phone_number = models.CharField(max_length=256, blank=False, null=False, verbose_name="Номер телефона")
    city = models.CharField(max_length=256, blank=False, null=False, verbose_name="Город проживания")
    _password = models.CharField(max_length=128, blank=False, null=False, verbose_name="Пароль")
    _remember_password = models.CharField(max_length=128, blank=False, null=False, verbose_name="Повторный пароль")

    def __str__(self):
        return "{} - {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Car(models.Model):
    """Модель автомобиля"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=256, blank=False, null=False, verbose_name="Марка")
    model = models.CharField(max_length=256, blank=False, null=False, verbose_name="Модель")
    body_type = models.CharField(max_length=256, blank=False, null=False, verbose_name="Тип кузова")
    year_issue = models.IntegerField(blank=False, null=False, verbose_name="Год выпуска")
    mileage = models.IntegerField(blank=True, null=True, verbose_name="Пробег")
    city = models.CharField(max_length=256, blank=False, null=False, verbose_name="Город")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    transmission = models.CharField(max_length=128, blank=False, null=False, verbose_name="Коробка передач")
    fuel = models.CharField(max_length=128, blank=False, null=False, verbose_name="Тип топлива")
    drive_unit = models.CharField(max_length=128, blank=False, null=False, verbose_name="Тип привода")
    engine_capacity = models.CharField(max_length=128, blank=False, null=False, verbose_name="Объем двигателя")
    engine_power = models.IntegerField(blank=False, null=False, verbose_name="Мощность двигателя")
    color_car = models.CharField(max_length=128, blank=False, null=False, verbose_name="Цвет авто")
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Цена авто ")

    def __str__(self):
        return "{} - {}".format(self.brand, self.model)

    class Meta:
        verbose_name = "Авто"
        verbose_name_plural = "Автомобили"


class Image(models.Model):
    """Фотографии автомобилей"""
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_images')

