from django.db import models

# Create your models here.
class User(models.Model):
  id = models.AutoField(primary_key=True)
  Name = models.CharField(max_length=100)
  Birthday = models.DateTimeField()
