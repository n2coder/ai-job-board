from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    industry = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name

