from django.db import models


class LogisticsOperator(models.Model):
    name = models.CharField(max_length=255)
