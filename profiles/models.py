"""
Contains models for app "profiles" : Profile
User model imported from Django without modifications
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Django model mapped to sqlite database
    Linked to User model (one-to-one)
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
