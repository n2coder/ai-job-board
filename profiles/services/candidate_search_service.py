from profiles.models import CandidateProfile
from ml_service.client import get_match_score


def search_candidates_for_job(job, min_score=0.0):
    """
    Returns candidates ranked by ML match score for a given job
    """

    candidates = CandidateProfile.objects.exclude(resume_text__isnull=True)

    results = []

    for candidate in candidates:
        if not candidate.resume_text:
            continue

        score = get_match_score(
            candidate_text=candidate.resume_text,
            job_text=job.job_description
        )

        if score >= min_score:
            results.append({
                "candidate": candidate,
                "match_score": round(score, 2)
            })

    # Sort by highest match score first
    results.sort(key=lambda x: x["match_score"], reverse=True)

    return results
