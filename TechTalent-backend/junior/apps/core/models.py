from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Base UserProfile class
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo_profil = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    is_student = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'


# Student model inheriting from UserProfile
class Student(UserProfile):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    numero_telephone = models.CharField(max_length=20)
    etablissement = models.CharField(max_length=255)
    filiere = models.CharField(max_length=255)
    niveau_etude = models.CharField(max_length=100)
    annee_graduation = models.IntegerField()
    type_recherche = models.CharField(max_length=255)
    date_disponibilite = models.DateField()
    cv = models.FileField(upload_to='student_cv/', blank=True, null=True)
    portfolio = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.nom} {self.prenom} (Student)'


# Company model inheriting from UserProfile
class Company(UserProfile):
    nom_societe = models.CharField(max_length=255)
    logo_societe = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    secteur_activite = models.CharField(max_length=255)
    description = models.TextField()
    site_web = models.URLField(blank=True, null=True)
    numero_telephone = models.CharField(max_length=20)
    adresse = models.CharField(max_length=255)
    taille_entreprise = models.CharField(max_length=100)
    annee_creation = models.IntegerField()

    def __str__(self):
        return f'{self.nom_societe} (Company)'

# Signal to set is_student to True when a Student is created
@receiver(post_save, sender=Student)
def set_is_student(sender, instance, created, **kwargs):
    if created:
        instance.user.profile.is_student = True
        instance.user.profile.save()

# Signal to set is_company to True when a Company is created
@receiver(post_save, sender=Company)
def set_is_company(sender, instance, created, **kwargs):
    if created:
        instance.user.profile.is_company = True
        instance.user.profile.save()



class JobOffer(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Brouillon'),
        ('published', 'Publié'),
    ]
    
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='job_offers_core')
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=500)
    details = models.TextField()
    full_description = models.TextField()
    required_skills = models.TextField()
    contract_type = models.CharField(max_length=100)
    work_mode = models.CharField(max_length=100)
    location = models.CharField(max_length=255, blank=True, null=True)
    offer_duration = models.CharField(max_length=100, blank=True, null=True)
    salary = models.CharField(max_length=100, blank=True, null=True)
    recruiter_name = models.CharField(max_length=255)
    recruiter_email = models.EmailField()
    recruiter_phone = models.CharField(max_length=20, blank=True, null=True)
    offer_image = models.ImageField(upload_to='job_offers/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.company.nom_societe}"