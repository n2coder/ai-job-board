from django.http import JsonResponse
from profiles.models import CandidateProfile
from jobs.services.job_search_service import search_jobs
from django.shortcuts import render
from .models import Job
from django.shortcuts import get_object_or_404
from .models import Job

def job_search_api(request):
    candidate_id = request.GET.get("candidate_id")
    query = request.GET.get("q")
    location = request.GET.get("location")

    candidate = CandidateProfile.objects.get(id=candidate_id)

    results = search_jobs(candidate, query, location)

    data = []
    for r in results:
        job = r["job"]
        data.append({
            "job_id": job.id,
            "title": job.title,
            "company": job.company.name,
            "location": job.location,
            "match_score": round(r["match_score"], 2)
        })

    return JsonResponse(data, safe=False)

def job_list_view(request):
    jobs = Job.objects.select_related("company").all().order_by("-created_at")
    return render(request, "jobs/job_list.html", {
        "jobs": jobs
    })
    
    
from django.shortcuts import render
from .models import Job, CATEGORY_CHOICES, JOB_TYPE_CHOICES
from django.db.models import Q


def job_search_view(request):
    jobs = Job.objects.filter(is_active=True).select_related("company")

    keyword = request.GET.get("keyword")
    location = request.GET.get("location")
    category = request.GET.get("category")
    job_type = request.GET.get("job_type")

    if keyword:
        jobs = jobs.filter(
            Q(title__icontains=keyword) |
            Q(must_have_skills__icontains=keyword) |
            Q(job_description__icontains=keyword)
        )

    if location:
        jobs = jobs.filter(location__icontains=location)

    if category:
        jobs = jobs.filter(category=category)

    if job_type:
        jobs = jobs.filter(job_type=job_type)

    context = {
        "jobs": jobs,
        "categories": CATEGORY_CHOICES,
        "job_types": JOB_TYPE_CHOICES,
        "filters": {
            "keyword": keyword or "",
            "location": location or "",
            "category": category or "",
            "job_type": job_type or "",
        }
    }

    return render(request, "jobs/job_search.html", context)


def job_detail_view(request, job_id):
    job = get_object_or_404(
        Job.objects.select_related("company"),
        id=job_id,
        is_active=True
    )

    # Placeholder – ML score comes later
    match_score = None
    if request.user.is_authenticated:
        match_score = "--"

    context = {
        "job": job,
        "match_score": match_score
    }

    return render(request, "jobs/job_detail.html", context)