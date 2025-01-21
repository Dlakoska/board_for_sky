from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """
    Модель пользователя
    """

    username = None
    first_name = models.CharField(max_length=30, verbose_name="Имя пользователя")
    last_name = models.CharField(max_length=30, verbose_name="Фамилия пользователя", **NULLABLE)
    phone = models.CharField(max_length=30, verbose_name="Телефон", **NULLABLE)
    email = models.EmailField(unique=True, verbose_name="Email")
    # добавил поле роли пользователя, false это user, true это админ
    role = models.BooleanField(default=False, verbose_name="Роль пользователя", **NULLABLE)
    image = models.ImageField(upload_to="board_for_sky/media/pictures", verbose_name="Аватарка", **NULLABLE)
    token = models.CharField(max_length=100, verbose_name='Токен', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

