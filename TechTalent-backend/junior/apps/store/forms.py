from django import forms
from .models import JobOffer,JobApplication


class JobOfferForm(forms.ModelForm):
    class Meta:
        model = JobOffer
        fields = [
            'category',
            'title',
            'slug',
            'description',
            'skills',
            'location',
            'job_type',
            'salary_range',
            'application_deadline',
        ]
        widgets = {
            'application_deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        
class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['resume', 'cover_letter', 'portfolio']
        widgets = {
            'cover_letter': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your cover letter here...'}),
            'portfolio': forms.URLInput(attrs={'placeholder': 'Portfolio URL (optional)'}),
        }
        labels = {
            'resume': 'Upload Resume',
            'cover_letter': 'Cover Letter',
            'portfolio': 'Portfolio (Optional)',
        }