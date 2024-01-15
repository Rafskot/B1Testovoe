# data_upload/models.py

from django.db import models


class BalanceSheet(models.Model):
    value_1 = models.FloatField()
    value_2 = models.FloatField()
    value_3 = models.FloatField()
    value_4 = models.FloatField()
    value_5 = models.FloatField()
    value_6 = models.FloatField()
    value_7 = models.FloatField()
    class_id = models.IntegerField()


class EndClass(models.Model):
    value_1 = models.CharField(max_length=255)
    value_2 = models.FloatField()
    value_3 = models.FloatField()
    value_4 = models.FloatField()
    value_5 = models.FloatField()
    value_6 = models.FloatField()
    value_7 = models.FloatField()
    class_id = models.IntegerField()


class EndTable(models.Model):
    value_1 = models.CharField(max_length=255)
    value_2 = models.FloatField()
    value_3 = models.FloatField()
    value_4 = models.FloatField()
    value_5 = models.FloatField()
    value_6 = models.FloatField()
    value_7 = models.FloatField()


class Class(models.Model):
    name = models.TextField()
