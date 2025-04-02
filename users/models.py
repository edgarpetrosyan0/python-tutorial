from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    username = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    password = models.CharField(max_length=256)

    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)  # Make sure to hash the password
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username  

    class Meta:  # Fix indentation of Meta class
        db_table = 'users'  