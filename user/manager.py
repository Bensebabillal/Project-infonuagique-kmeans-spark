from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
       """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)

        user = self.model(email=email, password=None, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(
            email=self.normalize_email(email),
            # username=username,
            password=password, **extra_fields
        )
        # user.email = username
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    # def create_superuser(self, email, password):
    #     """
    #     Create and save a SuperUser with the given email and password.
    #     """
    #
    #     if password is None:
    #         raise TypeError('Superusers must have a password.')
    #
    #     user = self.create_user(email, password)
    #     user.username = "admin-@" + generate_random_string()
    #     user.is_superuser = True
    #
    #     user.is_staff = True
    #
    #     user.save(using=self._db)
    #
    #     return user
