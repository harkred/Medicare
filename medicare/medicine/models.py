from django.db import models
from users.models import CustomUser

# Create your models here.
class Medicine(models.Model):
    med_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    med_name = models.CharField(max_length=100)
    med_dosage = models.CharField(max_length=100)
    med_frequency = models.CharField(max_length=100)
