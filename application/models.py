from django.db import models

# Create your models here.
class Registration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100,unique=True)
    
    def __str__(self):
        return self.first_name
