from django.db import models
from django.urls import reverse

# Create your models here.


class Car(models.Model):

    name = models.CharField(max_length=100)
    vin_number = models.CharField(max_length=100)
    car_model = models.ForeignKey(
        "car.CarModel",
        on_delete=models.SET_NULL,
        null=True,
        related_name="cars"
    )

    def company(self):
        if self.car_model:
            return self.car_model.company
        return None

    def __str__(self):
        return f"Name:{self.name} vin_number: {self.vin_number}"

    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ["car_model"]


class CarModel(models.Model):

    name = models.CharField(max_length=100)
    company = models.ForeignKey("car.Company", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('car_model-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ["name"]


class Company(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = "Companies"
        ordering = ["name"]
<<<<<<< HEAD
=======

    """
    Или можно так:
    class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        abstract = True
    
    Заменяем 'models.Model' на 'CommonInfo' и убираем 
    name = models.CharField(max_length=100) в каждом
    """
>>>>>>> dd0d35c29c3a5ab8b14dab41c28b1d8496529a76
