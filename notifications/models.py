from django.db import models

# Create your models here.

class Notified_list(models.Model):
    user_email =  models.EmailField(null=False)
    pincode = models.IntegerField(null = False)