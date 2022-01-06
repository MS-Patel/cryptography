# Generated by Django 4.0 on 2022-01-06 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nav', models.DecimalField(decimal_places=4, max_digits=20)),
                ('inserted_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserTransactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nav', models.DecimalField(decimal_places=4, max_digits=20)),
                ('units', models.DecimalField(decimal_places=4, max_digits=20)),
                ('portfolio', models.DecimalField(decimal_places=4, max_digits=20)),
                ('trx_date', models.DateTimeField(auto_now_add=True)),
                ('trx_type', models.CharField(max_length=50, verbose_name='Transaction Type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.account', verbose_name='USer')),
            ],
        ),
        migrations.CreateModel(
            name='UserPortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_units', models.DecimalField(decimal_places=2, max_digits=20)),
                ('total_portfolio', models.DecimalField(decimal_places=4, max_digits=20)),
                ('avg_nav', models.DecimalField(decimal_places=2, max_digits=20)),
                ('last_units', models.DecimalField(decimal_places=2, max_digits=20)),
                ('last_portfolio', models.DecimalField(decimal_places=4, max_digits=20)),
                ('last_nav', models.DecimalField(decimal_places=2, max_digits=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='account.account', verbose_name='User')),
            ],
        ),
    ]
