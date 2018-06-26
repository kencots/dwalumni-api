from django.db import models
from django.contrib.auth.models import User
from skill.models import Skill

class DetailSkill(models.Model):
    class Meta:
        db_table = "detail_skill"
    
    name = model.CharField(max_length=50)
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE
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

class UserDetailSkill(models.Model):
    class Meta:
        db_table = "detail_user_skill"
    
    skill_exam_detail = models.ForeignKey(
        DetailSkill,
        on_delete=models.CASCADE
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

