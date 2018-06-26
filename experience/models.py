from django.db import models
from django.contrib.auth.models import User

class Experience(models.Model):
    class Meta:
        db_table = "experience"
    
    name = models.CharField(max_length=45)
    job = models.CharField(max_length=45)
    beginning_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
