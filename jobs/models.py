from django.db import models
from django.conf import settings
from companies.models import Company

CATEGORY_CHOICES = [
    ("engineering", "Engineering"),
    ("data", "Data & AI"),
    ("marketing", "Marketing"),
    ("design", "Design"),
    ("hr", "HR"),
]

JOB_TYPE_CHOICES = [
    ("full_time", "Full-time"),
    ("part_time", "Part-time"),
    ("contract", "Contract"),
    ("internship", "Internship"),
]
class Job(models.Model):

    
    recruiter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posted_jobs'
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="jobs"
    )

    title = models.CharField(max_length=200)
    must_have_skills = models.TextField()
    experience_required = models.FloatField()
    location = models.CharField(max_length=100)
    job_description = models.TextField()
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="engineering"
    )
    job_type = models.CharField(
        max_length=50,
        choices=JOB_TYPE_CHOICES,
        default="full_time"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} | {self.company.name}"
