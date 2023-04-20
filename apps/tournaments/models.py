from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from auditlog.registry import auditlog
from ..common.models import BaseEntity
from ..clubs.models import Club


# Create your models here.

class Tournament(BaseEntity):
    name = models.CharField(max_length=100,unique=True)
    clubOrganizer = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


auditlog.register(Tournament)
