from django.db import models

# Create your models here.
class Contact(models.Model):
    number = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    message = models.CharField(max_length=100)
    date = models.DateField()
    
    def __str__(self):
        return self.email
    