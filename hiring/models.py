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