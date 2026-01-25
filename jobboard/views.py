from django.shortcuts import redirect

def home_redirect(request):
    if request.user.is_authenticated:
        if request.user.role == "candidate":
            return redirect("candidate_dashboard")
        elif request.user.role == "recruiter":
            return redirect("recruiter_dashboard")
    return redirect("landing")
