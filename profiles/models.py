from django.db import models
from django.conf import settings
from profiles.utils.resume_parser import extract_resume_text


class CandidateProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='candidate_profile'
    )

    full_name = models.CharField(max_length=100)
    experience_years = models.FloatField()
    location = models.CharField(max_length=100)
    notice_period_days = models.IntegerField()

# 🔽 Resume fields
    resume_file = models.FileField(
        upload_to='resumes/',
        blank=True,
        null=True
    )

    resume_text = models.TextField(
        blank=True,
        null=True
    )


    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.user.username})"



class RecruiterProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='recruiter_profile'
    )

    company_name = models.CharField(max_length=150)
    company_location = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return f"RecruiterProfile: {self.user.username}"
