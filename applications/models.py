from django.db import models
from django.conf import settings
from jobs.models import Job


class Application(models.Model):
    candidate = models.ForeignKey(
        "profiles.CandidateProfile",
        on_delete=models.CASCADE
    )
    job = models.ForeignKey(
        "jobs.Job",
        on_delete=models.CASCADE
    )

    match_score = models.FloatField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=[
            ("applied", "Applied"),
            ("shortlisted", "Shortlisted"),
            ("rejected", "Rejected"),
        ],
        default="applied"
    )

    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate} → {self.job}"
