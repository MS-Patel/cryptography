# Generated by Django 4.0 on 2022-01-20 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='tgid',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]
