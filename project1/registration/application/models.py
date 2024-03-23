from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    p_name=models.CharField(max_length=200)
    city=models.CharField(max_length=150)
    state=models.CharField(max_length=300)
    p_id=models.IntegerField(primary_key=True)
    uid=models.OneToOneField(User,on_delete=models.CASCADE)

class todoapp(models.Model):
    task=models.CharField(max_length=200)
    date=models.DateField()
    status=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)