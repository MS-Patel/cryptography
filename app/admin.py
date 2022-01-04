from django.contrib import admin
from .models import Coin
# Register your models here.


@admin.register(Coin)
class Coinadmin(admin.ModelAdmin):
    list_display = [
        'nav','inserted_date'
    ]

