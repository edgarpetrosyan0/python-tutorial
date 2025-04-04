from django.db import models
from django.contrib.auth.hashers import make_password

class Accounts(models.Model):
    username = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.username  

    class Meta:  # Fix indentation of Meta class
        db_table = 'accounts'  