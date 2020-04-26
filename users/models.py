from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):

    """ Coutom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = {
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    }

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    CURRENCY_USE = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = {
        (CURRENCY_USE, "USD"),
        (CURRENCY_KRW, "KRW"),
    }

    LANGUAGE_CHOICES = {(LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean")}

    아바타 = models.ImageField(blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, blank=True, null=True
    )
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, blank=True, null=True
    )
    currency = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=3, blank=True, null=True
    )
    superhost = models.BooleanField(default=False)


# https://docs.djangoproject.com/en/2.2/ref/models/fields/
