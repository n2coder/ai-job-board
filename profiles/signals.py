from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from .models import CandidateProfile, RecruiterProfile


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if not created:
        return

    if instance.role == 'candidate':
        CandidateProfile.objects.create(
            user=instance,
            full_name=instance.username,
            experience_years=0,
            location='',
            notice_period_days=0
        )

    elif instance.role == 'recruiter':
        RecruiterProfile.objects.create(
            user=instance,
            company_name='',
            company_location=''
        )
