from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager, UserRole
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractBaseUser):

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("id",)

    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = 'email'

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    email = models.EmailField(unique=True, max_length=100)
    role = models.CharField(max_length=5, choices=UserRole.choices, default=UserRole.USER)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    phone = PhoneNumberField()
    is_active = models.BooleanField(default=True)

    # также для работы модели пользователя должен быть переопределен
    # менеджер объектов
    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRole.ADMIN

    @property
    def is_user(self):
        return self.role == UserRole.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
