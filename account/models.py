from django.db import models
from datetime import datetime


class Account(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.username
