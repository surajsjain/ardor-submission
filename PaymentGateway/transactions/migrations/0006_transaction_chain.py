# Generated by Django 3.1 on 2020-08-14 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0005_transaction_transaction_res'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='chain',
            field=models.IntegerField(default=1),
        ),
    ]
