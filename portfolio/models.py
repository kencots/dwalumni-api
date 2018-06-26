from django.db import models
from django.contrib.auth.models import User
from skills.models import Skills

class Portfolios(models.Model):
    class Meta:
        db_table = 'portfolio'

    title       = models.CharField(max_length=128)
    desc        = models.TextField(blank=True, null=False)
    link_github = models.CharField(max_length=255)
    user     = models.ForeignKey(
        User,
        on_delete = models.CASCADE
    )
    skill    = models.ForeignKey(
        Skills,
        on_delete = models.CASCADE
    )
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