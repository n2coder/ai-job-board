from users.models import User
from profiles.models import CandidateProfile

def create_candidate(data, resume_file):
    if not data["email"]:
        return None, "Email not found"

    user, created = User.objects.get_or_create(
        email=data["email"],
        defaults={"username": data["email"].split("@")[0]}
    )

    if hasattr(user, "candidateprofile"):
        return None, "Candidate already exists"

    profile = CandidateProfile.objects.create(
        user=user,
        full_name=data["name"],
        experience_years=data["experience"],
        resume_text=data["resume_text"],
        resume_file=resume_file
    )

    return profile, None
