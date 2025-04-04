# models.py
import datetime
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    description = models.TextField()
    created_at = models.DateField(default=datetime.date.today)  

    def __str__(self):
        return self.title  

    class Meta:  # Fix indentation of Meta class
        db_table = 'blogs'  
