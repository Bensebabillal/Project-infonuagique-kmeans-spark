from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from osm_jet.fields import DjangoManyToMany


class CustomUser(AbstractUser):
    #     username = models.CharField(
    #         _('username'),
    #         max_length=150,
    #     )
    # email = models.EmailField(_('email address'), unique=True, )
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    # USERNAME_FIELD = 'email'
    # first_name = models.CharField(_('First name'), max_length=30, blank=True, )
    # last_name = models.CharField(_('Last name'), max_length=150, blank=True, )
    #
    # profile_type = models.CharField(
    #     _("Type"), max_length=50, choices=Types.choices, default=base_type
    # )
    avatar = models.FileField("avatar", upload_to='image/avatar', default='image/avatar-default.jpg', blank=True, )
    groups = DjangoManyToMany(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        # related_name="user_set",
        related_query_name="user",
    )
    user_permissions = DjangoManyToMany(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        # related_name="user_set",
        related_query_name="user",
    )

    # for upload document file
    # document_file = models.ImageField()

    REQUIRED_FIELDS = []

    # objects = CustomUserManager()

    def __str__(self):
        return self.email
