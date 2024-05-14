from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class User(models.Model):
    usr_id = models.AutoField(primary_key=True)
    usr_name = models.CharField(max_length=200)
    usr_last_name = models.CharField(max_length=200)
    usr_gener = models.CharField(max_length=50)
    usr_email = models.EmailField(max_length=150)
    usr_password = models.CharField(max_length=50)
    usr_address = models.CharField(max_length=200)
    usr_phone = models.CharField(max_length=200)
    usr_last_access = models.DateTimeField(auto_now=True)