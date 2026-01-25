from django.contrib import admin
from .models import Application
from .utils.ml_client import get_match_score


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("candidate", "job", "match_score", "status")
    list_filter = ("status",)
    readonly_fields = ("match_score",)

    def save_model(self, request, obj, form, change):
        # Run ML scoring only when creating a new application
        if not change:
            resume_text = obj.candidate.resume_text
            job_text = obj.job.job_description

            if resume_text and job_text:
                obj.match_score = get_match_score(
                    resume_text=resume_text,
                    job_text=job_text
                )

        super().save_model(request, obj, form, change)
