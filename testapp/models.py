from django.db import models

from django.urls import reverse

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=64)
    total_emp = models.IntegerField()
    address = models.CharField(max_length=64)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse("List")
