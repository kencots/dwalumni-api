from django.db import models
from django.contrib.auth.models import User
from skills.models import Skills

class OverallSkills(models.Model):
    class Meta:
        db_table = "skill_exam_overall"

    name = models.CharField(max_length=50)
    skill = models.ForeignKey(
        Skills,
        on_delete=models.CASCADE
    )

class UserOverallSkills(models.Model):
    class Meta:
        db_table = "user_overall_skills"

    overall_skill = models.ForeignKey(
        OverallSkills,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    score = models.SmallIntegerField() 
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