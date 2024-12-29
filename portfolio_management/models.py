# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Stocks(models.Model):
    stock_id = models.IntegerField(primary_key=True)
    symbol = models.CharField(max_length=10)
    company_name = models.CharField(max_length=100)
    sector = models.CharField(max_length=50, blank=True, null=True)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    daily_volume = models.BigIntegerField()
    market_cap = models.DecimalField(max_digits=15, decimal_places=2)
    pe_ratio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dividend_yield = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stocks'
