from django.contrib import admin
from .models import Coin, Feedback, UserPortfolio, UserTransactions
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
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'

@admin.register(UserTransactions)
class trxadmin(admin.ModelAdmin):
    list_display = [
        'user','nav','units','portfolio','trx_date','trx_type'
    ]    