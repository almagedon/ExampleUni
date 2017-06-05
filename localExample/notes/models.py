from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Notes(models.Model):

    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        verbose_name="Usuario De la nota"
    )
    author = models.CharField(
            max_length=500,
            verbose_name="autor"
    )
    title = models.CharField(
            max_length=500,
            unique=True,
            verbose_name="Titulo"
    )
    note = models.TextField(
            verbose_name="Note"
        )
    created_date = models.DateTimeField(
                default=timezone.now
        )

    class Meta:
        db_table = 'Notes'
        ordering = ["title"]
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return '%s (%s)' % (
            self.author,
            self.title,
        )

    def __unicode__(self):
        return '%s (%s)' % (
            self.author,
            self.title,
        )

