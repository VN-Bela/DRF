from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    roll = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    state= models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name