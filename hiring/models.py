from django.db import models
from django.contrib.auth.models import User
from company.models import Company

class Hiring(models.Model):
    class Meta:
        db_table = "hiring"

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE
    )
    is_active = models.BooleanField(initial=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='unit_created_by'
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='unit_updated_by'
    )