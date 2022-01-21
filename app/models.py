from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DateTimeField
from account.models import Account 

# Create your models here.


class Coin(models.Model):
    nav = models.DecimalField(max_digits=20,decimal_places=4)
    inserted_date = models.DateTimeField(auto_now_add=True)


class UserPortfolio(models.Model):

    user = models.OneToOneField(Account, verbose_name="User", on_delete=models.PROTECT)
    total_units = models.DecimalField(max_digits=20,decimal_places=2)
    total_portfolio = models.DecimalField(max_digits=20,decimal_places=4)
    avg_nav = models.DecimalField(max_digits=20,decimal_places=2)
    last_units = models.DecimalField(max_digits=20,decimal_places=2)
    last_portfolio = models.DecimalField(max_digits=20,decimal_places=4)
    last_nav = models.DecimalField(max_digits=20,decimal_places=2) 

class UserTransactions(models.Model):

    user = models.ForeignKey(Account,verbose_name="USer", on_delete=models.PROTECT)
    nav = models.DecimalField(max_digits=20,decimal_places=4)
    units = models.DecimalField(max_digits=20,decimal_places=4)
    portfolio = models.DecimalField(max_digits=20,decimal_places=4)
    trx_date = DateTimeField(auto_now_add=True)
    trx_type = models.CharField(verbose_name="Transaction Type", max_length=50)


class Feedback(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the sender")
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Feedback"

    def __str__(self):
        return self.name + "-" +  self.email