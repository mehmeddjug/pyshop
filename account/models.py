from django.db import models


class AccountManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class Account(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    active = AccountManager()

    def __str__(self):
        return self.username
