# models.py
import datetime
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=256)
    reting = models.IntegerField()
    description = models.TextField()
    imageUrl = models.URLField()
    created_at = models.DateField(default=datetime.date.today)  
    
    def __str__(self):
        return self.title  

    class Meta:  # Fix indentation of Meta class
        db_table = 'products'   
