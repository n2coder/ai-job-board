from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from jobboard.views import home_redirect

urlpatterns = [
    path("admin/", admin.site.urls),

    # Auth (login, logout)
    path("accounts/", include("django.contrib.auth.urls")),

    # Landing page
    path(
        "",
        TemplateView.as_view(template_name="public/landing.html"),
        name="landing",
    ),
    path("register/", user_views.register, name="register"),
    path("", home_redirect, name="home"),
    path("auth/", include("users.urls")),
    path("users/", include("users.urls")),
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="public/landing.html"), name="landing"),
    path("", include("jobs.urls")),
    path("users/", include("users.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

