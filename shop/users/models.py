from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class YandexUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    yandex_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.yandex_id