"""
Contains models for app "lettings" : Address & Letting
"""
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Django model mapped to sqlite database
    Address used for Letting's object (one-to-one)
    Pluralization managed with Meta class
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f'{self.number} {self.street}'

    class Meta:
        verbose_name_plural = 'Addresses'


class Letting(models.Model):
    """
    Django model mapped to sqlite database
    Linked to Address (one-to-one)
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
