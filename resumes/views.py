from django.shortcuts import render
from .forms import ResumeUploadForm
from .services.text_extractor import extract_text
from .services.resume_parser import parse_resume
from .services.candidate_creator import create_candidate

def bulk_upload_resumes(request):
    summary = []

    if request.method == "POST":
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            for file in request.FILES.getlist("resumes"):
                text = extract_text(file.temporary_file_path())
                parsed = parse_resume(text)
                profile, error = create_candidate(parsed, file)

                summary.append({
                    "file": file.name,
                    "status": "Created" if profile else "Failed",
                    "reason": error
                })
    else:
        form = ResumeUploadForm()

    return render(request, "resumes/upload.html", {
        "form": form,
        "summary": summary
    })
