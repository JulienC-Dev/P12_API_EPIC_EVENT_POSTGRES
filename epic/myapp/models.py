from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    pass


class Client(models.Model):
    first_name = models.CharField(max_length=28)
    last_name = models.CharField(max_length=28)
    email = models.EmailField(max_length=28)
    compagny = models.CharField(max_length=28)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. "
                                         "Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # Validators should be a list
    date_creation = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    prospect = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name}'


class Contract(models.Model):
    TYPE_STATUS = (
        ('nonsigne', _('Non signé')),
        ('signe', _('Signé')),
    )

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=28)
    amount = models.IntegerField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_signature = models.DateTimeField(null=True, blank=True)
    status = models.CharField(choices=TYPE_STATUS, max_length=28, default='nonsigne')

    def __str__(self):
        return f'{self.client}'


class Evenement(models.Model):
    TYPE_EVENT = (
        ('anniversaire', _('Anniversaire')),
        ('mariage', _('Mariage')),
        ('nouvelan', _('Nouvel an')),
    )
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, verbose_name="client contract")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='personnel_assignee',
                             verbose_name="employee")
    title = models.CharField(max_length=28)
    type = models.CharField(choices=TYPE_EVENT, max_length=28, default="anniversaire")
    description = models.CharField(max_length=28)
    localisation = models.IntegerField()
    date_event_begin = models.DateTimeField()
    date_event_end = models.DateTimeField()

    def __str__(self):
        return f'{self.title}'



