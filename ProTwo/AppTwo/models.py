from django.db import models

# Create your models here.
class User(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254, unique=True)

class a(models.Model):
    Test = models.CharField(max_length=50)