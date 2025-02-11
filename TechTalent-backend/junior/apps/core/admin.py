from .models import Student,Company,UserProfile
from django.contrib import admin

admin.site.register(UserProfile)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'user')  # Display associated user explicitly

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('nom_societe', 'user')  # Display associated user explicitly
