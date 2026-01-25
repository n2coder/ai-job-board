from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "company",
        "category",
        "job_type",
        "location",
        "experience_required",
        "is_active",
        "created_at",
    )

    list_filter = ("category", "job_type", "location", "is_active")
    search_fields = ("title", "must_have_skills", "job_description")
