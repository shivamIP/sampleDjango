from django.db import models

# Create your models here.

class Applicant(models.Model):
    name = models.CharField(max_length=30)
    mail = models.EmailField(unique=True)
    phone = models.IntegerField(max_length=10,unique=True)
    exp = models.CharField(max_length=2)
    domain = models.CharField(max_length=10)
    cv = models.FilePathField(max_length=30)
    status = models.CharField(max_length=10, default='Processing')