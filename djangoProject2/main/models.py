from django.db import models

# Create your models here.

class CalcHistory(models.Model):
    id = models.IntegerField(
        max_length=123,
        verbose_name='номер',
    )
    val1 = models.CharField(
        max_length=123,
        verbose_name='10',
    )
    val2 = models.CharField(
        default=0,
        verbose_name='20',
    )
    created_at = models.CharField(
        max_length=123,
        verbose_name='выполнено на',
    )
    result = models.CharField(
        max_length=123,
        verbose_name='результат',
    )
    operator = models.IntegerField(
        default=0,
        verbose_name='оператор',
    )

