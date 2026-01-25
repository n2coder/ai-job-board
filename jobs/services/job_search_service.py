from jobs.models import Job
from ml_service.client import get_match_score

def search_jobs(candidate, query=None, location=None):
    qs = Job.objects.filter(is_active=True)

    if query:
        qs = qs.filter(title__icontains=query)

    if location:
        qs = qs.filter(location__icontains=location)

    results = []

    for job in qs:
        score = get_match_score(
            candidate_text=candidate.resume_text,
            job_text=job.job_description
        )

        results.append({
            "job": job,
            "match_score": round(score, 2)
        })

    # Sort by score (highest first)
    results.sort(key=lambda x: x["match_score"], reverse=True)

    return results
