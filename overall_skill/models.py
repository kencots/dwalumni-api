from django.db import models
from django.contrib.auth.models import User
from skill.models import Skill

class OverallSkill(models.Model):
    class Meta:
        db_table = "skill_exam_overall"

    name = models.CharField(max_length=50)
    skill = models.ForeignKey(
        Skill,
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
        related_name='overall_skill_created_by'
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='overall_skill_updated_by'
    )

class UserOverallSkill(models.Model):
    class Meta:
        db_table = "user_overall_skill"

    overall_skill = models.ForeignKey(
        OverallSkill,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    score = models.SmallIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_overall_skill_created_by'
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_overall_skill_updated_by'
    )
