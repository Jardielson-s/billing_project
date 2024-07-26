# Generated by Django 4.1.13 on 2024-07-26 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='bill',
            index=models.Index(fields=['government_id', 'email', 'debt_id'], name='billing_bil_governm_96b1ea_idx'),
        ),
        migrations.AddConstraint(
            model_name='bill',
            constraint=models.UniqueConstraint(fields=('government_id', 'email', 'debt_id'), name='billing_bill_unique'),
        ),
    ]