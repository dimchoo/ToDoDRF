from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password

PHONE_REGEX = r'^\+?1?\d{9,15}$'
PHONE_VALIDATOR_MSG = 'Phone number must be entered in the format: "+999999999". Up to 15 digits allowed.'
PHONE_REGEX_VALIDATOR = RegexValidator(regex=PHONE_REGEX, message=PHONE_VALIDATOR_MSG)


class UserDRF(AbstractUser):
    email = models.EmailField(unique=True)
    photo = models.ImageField('Фото', upload_to='photos', blank=True)
    phone_number = models.CharField('Номер телефона', validators=[PHONE_REGEX_VALIDATOR, ], max_length=17, blank=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(UserDRF, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Юзер'
        verbose_name_plural = 'Юзеры'
