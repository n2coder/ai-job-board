from django.contrib import admin
from .models import CandidateProfile, RecruiterProfile
from profiles.utils.resume_parser import extract_resume_text


@admin.register(CandidateProfile)
class CandidateProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'experience_years',
        'location',
        'notice_period_days',
    )

    search_fields = ('user__username', 'location')
    readonly_fields = ('resume_text',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        if obj.resume_file:
            try:
                print("Parsing resume (admin):", obj.resume_file.path)
                text = extract_resume_text(obj.resume_file.path)

                if text and text != obj.resume_text:
                    obj.resume_text = text
                    obj.save(update_fields=["resume_text"])
                    print("Resume text extracted successfully (admin)")

            except Exception as e:
                print("Resume parsing failed (admin):", e)




@admin.register(RecruiterProfile)
class RecruiterProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'company_location')
    search_fields = ('user__username', 'company_name')

