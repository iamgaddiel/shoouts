from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField



class User(AbstractUser):
    ACCOUNT_CATEGORY = [
        ('creator', 'creator'),
        ('client', 'client'),
    ]

    ACCOUNT_TAG =[
        ('songwriter', 'songwriter'),
        ('producer', 'producer'),
        ('artist', 'artist'),
        ('label', 'label'),
        ('manager', 'manager'),
    ]

    email = models.EmailField(unique=True)
    phone = models.CharField(unique=True, max_length=20)
    country = CountryField()
    sate = models.CharField(max_length=30)
    city = models.CharField(max_length=40)
    zipcode = models.CharField(max_length=40)
    account_category = models.CharField(max_length=20, choices=ACCOUNT_CATEGORY)
    account_tag = models.CharField(max_length=20, choices=ACCOUNT_TAG)
    profile_image = models.ImageField(default='profile.jpg')

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']


    def __str__(self) -> str:
        return self.username


