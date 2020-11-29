from django.db import models
from tools.functions_a import date

# Create your models here.
class ticket(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=100)

    content = models.TextField(max_length=3500)
    created_date = models.DateTimeField(default=date())
    changed_date = models.DateTimeField(default=date())
    owner = models.CharField(max_length=150)
    supporter = models.CharField(max_length=150)

    def __str__(self):
        return "Ticker description: {}".format(self.description)

class issues_comboBox(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
