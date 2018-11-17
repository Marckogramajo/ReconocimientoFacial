# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.
class Records(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, null=True)
    pais = models.CharField(max_length=50, null=True)
    ocupacion = models.CharField(max_length=150, null=True)
    bio = models.TextField()
    recorded_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Records"
