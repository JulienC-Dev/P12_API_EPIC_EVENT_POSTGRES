from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone as tz


class CustomEmployee(AbstractUser):
    is_staff = models.BooleanField(default=True)


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
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


def validate_date(date_signature):
    if date_signature < tz.now():
        raise ValidationError("Date cannot be in the past")


class Contract(models.Model):
    TYPE_STATUS = (
        ('nonsigne', _('Non signé')),
        ('signe', _('Signé')),
    )
    contrat_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=28)
    amount = models.IntegerField(validators=[MinValueValidator(1000)])
    date_creation = models.DateTimeField(auto_now_add=True)
    date_signature = models.DateTimeField(validators=[validate_date], null=True, blank=True)
    status = models.CharField(choices=TYPE_STATUS, max_length=28, default='nonsigne')

    def __str__(self):
        return f'{self.contrat_id}'


@receiver(post_save, sender=Contract)
def event_created_with_new_contract(sender, instance, **kwargs):
    if instance.evenement_set.count() == 0:
        Evenement(contract=instance).save()


class Evenement(models.Model):
    TYPE_EVENT = (
        ('anniversaire', _('Anniversaire')),
        ('mariage', _('Mariage')),
        ('nouvelan', _('Nouvel an')),
    )
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    employee = models.ForeignKey(CustomEmployee, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=28, null=True, blank=True)
    type = models.CharField(choices=TYPE_EVENT, max_length=28, default="anniversaire")
    description = models.CharField(max_length=28, null=True, blank=True)
    localisation = models.IntegerField(null=True, blank=True)
    date_event_begin = models.DateTimeField(null=True, blank=True)
    date_event_end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}'



