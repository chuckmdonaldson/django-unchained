from django.db import models
from django import forms
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField("Category Name",max_length=20,unique=True)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    name = models.CharField("Schedule Name",max_length=20,unique=True)

    def __str__(self):
        return self.name

class PaymentProvider(models.Model):
    name = models.CharField("Provider Name",max_length=20,unique=True)

    def __str__(self):
        return self.name

class PaymentMethod(models.Model):
    name        = models.ForeignKey(PaymentProvider,on_delete=models.CASCADE,related_name='providers')
    card_number = models.CharField("Card Number",max_length=16)
    exp_date    = models.DateField("Expiration Date")
    cvv         = models.CharField("CVV",max_length=3)

    def __str__(self):
        return str(self.name)

class Creditor(models.Model):
    name           = models.CharField("Creditor Name",max_length=50,unique=True)
    url            = models.URLField("URL",unique=True)       # form_widget=URLInput
    account_number = models.CharField("Account Number",max_length=20)
    username       = models.CharField(max_length=30)
    password       = models.CharField(max_length=16)
    category       = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categories')
    autopay        = models.BooleanField(default=False)
    schedule       = models.ForeignKey(Schedule,on_delete=models.CASCADE,related_name='schedules')
    payment_method = models.ForeignKey(PaymentMethod,on_delete=models.CASCADE,related_name='methods')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("bills:creditor_detail",kwargs={'pk':self.pk})
