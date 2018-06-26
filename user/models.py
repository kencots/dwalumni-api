from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    class Meta:
        db_table = "profile"
    
    gender = (
        ('M', 'Male'),
        ('F', 'Female'),
    )    
    birthdate = models.DateTimeField()
    about = models.CharField(max_length=255)
    address = models.CharField()
    expectation_salary = models.FloatField()
    expectation_work_location = models.CharField(max_length=255)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )    