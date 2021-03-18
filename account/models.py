from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User,verbose_name="Пользователь", on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name="Имя", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия", max_length=50)
    parent_name = models.CharField(verbose_name="Отчество", max_length=50)
    email = models.EmailField("Email")
    password = models.CharField("Пароль", max_length=50)
    date_of_birth = models.DateField()
    SEX_LIST = (
        (1, "Мужской"),
        (2, "Женский")
    )
    sex = models.IntegerField(verbose_name="Пол", choices=SEX_LIST)
    phone_number = models.IntegerField(verbose_name="Телефонный номер", unique=True)
    stir = models.IntegerField(verbose_name="ИНН", unique=True)
    PERSON_LIST = (
        (1, "Физическое лицо"),
        (2, "Юридическое лицо")
    )
    person = models.IntegerField(verbose_name="Принадлежность лица", choices=PERSON_LIST)
    passport = models.CharField(verbose_name="Паспортные данные", max_length=10, unique=True)
    date_of_passport = models.DateField()
    passport_issued_by = models.CharField(verbose_name="Кем выдан паспорт", max_length=100)
    pinfl = models.IntegerField(verbose_name="ПИНФЛ")
    region = models.CharField(verbose_name="Регион", max_length=15)
    area = models.CharField(verbose_name="Район", max_length=20)
    address = models.CharField(verbose_name="Адрес", max_length=120)

    #if juridic person
    organizatsion = models.CharField(verbose_name="Наименование организации", null=True, blank=True, unique=True, max_length=100)
    stir_yur = models.PositiveIntegerField(verbose_name="ИНН юр лица", null=True, blank=True, unique=True)

    def __str__(self):
        return self.user.username