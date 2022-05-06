from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone as tz
from django.contrib.auth.models import AbstractUser


class CustomEmployee(AbstractUser):
    is_staff = models.BooleanField(default=True)


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(CustomEmployee, on_delete=models.SET_NULL, null=True, blank=True)
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
        return f'{self.client_id}'


def date_check(value):
    if value < tz.now():
        raise ValidationError("Vous ne pouvez pas réserver une date antérieur")


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
    date_signature = models.DateTimeField(validators=[date_check], null=True, blank=True)
    status = models.CharField(choices=TYPE_STATUS, max_length=28, default='nonsigne')

    class Meta:
        unique_together = ['client', 'name']

    def clean(self):
        if self.date_signature is None and self.status == "signe":
            raise ValidationError('Le contrat ne peut être signé sans date')
        if self.date_signature is not None and self.status == "nonsigne":
            raise ValidationError('Le contrat doit être en status signé ')

    def __str__(self):
        return f'{self.contrat_id}'


@receiver(post_save, sender=Contract)
def event_created_new_contract(sender, instance, **kwargs):
    if instance.evenement_set.count() == 0 and instance.status =="signe":
        instance.client.prospect = False
        instance.client.save()
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
    ville = models.CharField(max_length=28, null=True, blank=True)
    date_event_begin = models.DateTimeField(validators=[date_check], null=True, blank=True)
    date_event_end = models.DateTimeField(validators=[date_check], null=True, blank=True)

    class Meta:
        unique_together = ['contract', ]

    def clean(self):
        if self.contract.status == "nonsigne":
            raise ValidationError("Veuillez signer le contrat")
        if self.date_event_end is None and self.date_event_begin is not None:
            raise ValidationError("Veuillez saisir une date de fin d'événement")
        if self.date_event_end is not None and self.date_event_begin is None:
            raise ValidationError("Veuillez saisir une date de début d'événement")

    def __str__(self):
        return f'{self.title}'