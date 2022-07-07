from django.db import models


class Service(models.Model):
    """
    Предоставляемые услуги
    """
    name = models.CharField('имя', max_length=64)
    photo = models.ImageField('фото', upload_to='services/')
    description = models.CharField('описание', max_length=1000)

    class Meta:
        verbose_name = "сервис"
        verbose_name_plural = "сервисы"


class Worker(models.Model):
    """
    Члены команды
    """
    name = models.CharField('имя', max_length=100)
    photo = models.ImageField('фото', upload_to='workers/')
    work_experience = models.IntegerField('стаж')
    description = models.CharField('описание', max_length=300)

    class Meta:
        verbose_name = "сотрудник"
        verbose_name_plural = "сотрудники"


class Client(models.Model):
    """
    Клиенты и их отзывы
    """
    name = models.CharField('имя', max_length=100)
    photo = models.ImageField('фото', upload_to='clients/')
    review = models.CharField('отзыв', max_length=300)

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"


class Case(models.Model):
    """
    Реализованные кейсы
    """
    case = models.FileField('дело', upload_to='cases/')

    class Meta:
        verbose_name = "кейс"
        verbose_name_plural = "кейсы"


class Request(models.Model):
    """
    Заявки от пользователей
    """
    name = models.CharField('имя', max_length=100)
    phone_number = models.IntegerField('номер')
    request = models.CharField('вопрос', max_length=500)

    class Meta:
        verbose_name = "заявка"
        verbose_name_plural = "заявки"
