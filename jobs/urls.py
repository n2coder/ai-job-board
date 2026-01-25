from django.urls import path
from .views import job_search_api
from .views import job_list_view
from .views import job_search_view
from .views import job_detail_view

urlpatterns = [
    path("api/jobs/search/", job_search_api),
    path("jobs/", job_list_view, name="job_list"),
    path("search/", job_search_view, name="job_search"),
    path("jobs/", job_search_view, name="job_search"),
    path("jobs/<int:job_id>/", job_detail_view, name="job_detail"),
]
