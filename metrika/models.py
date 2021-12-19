from django.db import models
from core.models import BaseModel


class Statistics(BaseModel):
    class Meta:
        verbose_name = "Статистика"
        verbose_name_plural = "Статистика"

    date = models.DateField(verbose_name="Дата")
    views = models.PositiveIntegerField(verbose_name="Просмотры",
                                        null=True, blank=True)
    clicks = models.PositiveIntegerField(verbose_name="Клики",
                                         null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2,
                               verbose_name="Цена",
                               null=True, blank=True)
