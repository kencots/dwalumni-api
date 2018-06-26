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
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='experience_created_by'
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='experience_updated_by'
    )
