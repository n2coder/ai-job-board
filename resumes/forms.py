from django import forms

class ResumeUploadForm(forms.Form):
    resumes = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True})
    )
