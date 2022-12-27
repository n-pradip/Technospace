from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, terms_and_condition, password=None, password2=None):
        """
        Creates and saves a User with the given email,terms_and_condition and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            terms_and_condition=terms_and_condition,
            # password=password,
        )

        user.set_password(make_password(password))
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, terms_and_condition, password=None):
        """
        Creates and saves a superuser with the given full_name,
        email, full_name, phone_no, terms_and_condition,
        """
        user = self.create_user(
            email,
            full_name=full_name,
            terms_and_condition=terms_and_condition,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    full_name = models.CharField(max_length=128)
    terms_and_condition = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'phone_no', 'terms_and_condition']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin