from django.contrib.auth.models import AbstractUser
from django.db import models

SUBSCRIBER = "SUBSCRIBER"
AUTHOR = "AUTHOR"
ROLE_CHOICES = [
    (SUBSCRIBER, "Подписчик"),
    (AUTHOR, "Автор"),
]


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Email")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=SUBSCRIBER,
                            verbose_name="Роль")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
