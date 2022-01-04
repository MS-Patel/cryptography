from django.contrib import admin
from .models import Coin, UserPortfolio
# Register your models here.


@admin.register(Coin)
class Coinadmin(admin.ModelAdmin):
    list_display = [
        'nav','inserted_date'
    ]

@admin.register(UserPortfolio)
class Useradmin(admin.ModelAdmin):
    list_display = [
        'user','total_units','total_portfolio','last_portfolio'
    ]

