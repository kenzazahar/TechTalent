from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django import forms
from .models import Student,Company,UserProfile,User # Custom User model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    
class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class StudentForm(forms.ModelForm):
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Student
        fields = [
            'nom', 'prenom', 'numero_telephone', 'photo_profil',
            'etablissement', 'filiere', 'niveau_etude', 'annee_graduation',
            'type_recherche', 'date_disponibilite', 'cv', 'portfolio'
        ]

class CompanyForm(forms.ModelForm):
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Company
        fields = [
            'nom_societe', 'logo_societe', 'secteur_activite', 'description',
            'site_web', 'numero_telephone', 'adresse', 'taille_entreprise', 'annee_creation'
        ]
        
class EditCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'nom_societe', 'logo_societe', 'secteur_activite', 'description',
            'site_web', 'numero_telephone', 'adresse', 'taille_entreprise', 'annee_creation'
        ]
class EditStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'numero_telephone', 'photo_profil',
            'etablissement', 'filiere', 'niveau_etude', 'annee_graduation',
            'type_recherche', 'date_disponibilite', 'cv', 'portfolio'
        ]

