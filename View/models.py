from django.db import models

class Student(models.Model):
    Uname = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    
