# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils import six, timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from utils import file_rename
# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, nickname, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not nickname:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, nickname=nickname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, nickname, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, nickname, password, **extra_fields)

    def create_superuser(self, email, nickname, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, nickname, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_(u'邮箱'), max_length=255, unique=True)
    nickname = models.CharField(_(u'别名'), max_length=30, unique=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    avatar = models.ImageField(_(u'头像'), upload_to=file_rename('avatars/'), null=True, blank=True,
                               help_text=_('user avatar'))
    date_joined = models.DateTimeField(_('注册时间'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        return self.nickname

    def get_short_name(self):
        return self.nickname

    def __unicode__(self):
        return self.nickname


class TimeStampedModel(models.Model):
    create_time = models.DateTimeField(auto_created=True)
    modify_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserInfo(TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    sign = models.CharField(_(u'签名'), blank=True, max_length=50)
    slogan = models.TextField(_(u'个人简介'), blank=True)
    city = models.CharField(_(u'常居地'), blank=True, max_length=20)
    company = models.CharField(_(u'公司'), blank=True, max_length=50)
    position = models.CharField(_(u'职位'),  blank=True, max_length=20)


class LoginInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    ip_address = models.GenericIPAddressField(default='0.0.0.0')
    login_time = models.DateTimeField(auto_now_add=True)


class ContactIM(models.Model):
    IM_TYPE_CHOICES = (
        ('WB', u'微博'),
        ('ZH', u'知乎'),
        ('DB', u'豆瓣'),
        ('OT', u'其他'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    im_type = models.CharField(max_length=15, choices=IM_TYPE_CHOICES)
    link = models.URLField()

    class Meta:
        unique_together = ("user", "im_type")
















# # TODO 支持手机登陆
# CELL_RE = r'^1[34578]\d{9}$'
#
#
# class User_Extend(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL)
#     # TODO支持手机号,默认中国区手机号
#     cellphone = models.CharField(_('username'), max_length=11, unique=True,
#                                  validators=[validators.RegexValidator(
#                                      CELL_RE, _('Enter a valid china cellphone number.')),
#                                  ],
#                                  help_text=_('Require a valid china cellphone number'),
#                                  error_messages={
#                                      'unique': _("A user with that cellphone already exists."), },
#                                  )


