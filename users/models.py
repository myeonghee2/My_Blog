from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, date_of_birth=None, nickname=None, fullname=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")
        if not nickname:
            raise ValueError("Users must have a nickname")
        if not fullname:
            raise ValueError("Users must have a fullname")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            date_of_birth=date_of_birth,
            nickname=nickname,
            fullname=fullname
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, nickname=None, fullname=None):

        user = self.create_user(
            username,
            email,
            password=password,
            nickname=nickname,
            fullname=fullname,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(
        verbose_name="username",
        max_length=50,
        unique=True,
    )

    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )

    nickname = models.CharField(
        verbose_name="nickname",
        max_length=50,
        unique=True,
    )

    fullname = models.CharField(
        verbose_name="fullname",
        max_length=50,
        unique=True,
    )

    date_of_birth = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "nickname", "fullname"]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin