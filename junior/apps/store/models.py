from django.db import models
from django.apps import apps

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class JobOffer(models.Model):
    INTERNSHIP = 'internship'
    ENTRY_LEVEL = 'entry_level'

    JOB_TYPE_CHOICES = [
        (INTERNSHIP, 'Internship'),
        (ENTRY_LEVEL, 'Entry-Level'),
    ]

    category = models.ForeignKey(Category, related_name='job_offers', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    company = models.ForeignKey('core.Company', related_name='job_offers', on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill, related_name='job_offers', blank=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, default='internship')
    salary_range = models.CharField(max_length=50, blank=True, null=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    application_deadline = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Job Offers'
        ordering = ['-posted_on']

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('waiting', 'Waiting'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    student = models.ForeignKey('core.Student', related_name='applications', on_delete=models.CASCADE)
    job_offer = models.ForeignKey(JobOffer, related_name='applications', on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='waiting')
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(blank=True, null=True)  # Optional
    portfolio = models.URLField(blank=True, null=True)  # Optional

    class Meta:
        verbose_name_plural = 'Job Applications'
        unique_together = ['student', 'job_offer']  # Prevent duplicate applications
        ordering = ['-applied_on']

    def __str__(self):
        return f"{self.student.user.username} - {self.job_offer.title}"