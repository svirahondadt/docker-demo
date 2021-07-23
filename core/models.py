from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True,unique=True)
    ruc = models.CharField(max_length=150, blank=True, null=True,unique=True)
    creation_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

