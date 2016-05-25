from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

# Create your models here.


class Cards(models.Model):
    card_title = models.CharField(
        max_length=255,
        blank=False,
        null=False)
    card_description = models.TextField(
        blank=False,
        null=False,
        verbose_name='card_description')
    card_created_on = models.DateTimeField(
        'date published',
        default=timezone.now)

    def __unicode__(self):
        """Unicode Method to display Relevent data."""
        return self.card_title

    class Meta:
        """info about the class."""

        verbose_name = "Card"
        verbose_name_plural = "Cards"
