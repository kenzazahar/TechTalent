from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from .forms import StudentForm, CompanyForm, EditCompanyForm, CustomUserForm, LoginForm, EditStudentForm
from .models import Company, Student, User, UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
import json

# API Login View for Vue.js Frontend
@csrf_exempt
def api_login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            
            # Authenticate user
            user = authenticate(username=username, password=password)
            
            if user is not None:
                if not user.is_active:
                    return JsonResponse({
                        'error': 'Compte utilisateur désactivé'
                    }, status=403)
                
                # Check for user profile
                user_type = None
                profile = None
                
                try:
                    # Try to get student profile
                    profile = Student.objects.get(user=user)
                    user_type = 'student'
                except Student.DoesNotExist:
                    try:
                        # Try to get company profile
                        profile = Company.objects.get(user=user)
                        user_type = 'company'
                    except Company.DoesNotExist:
                        return JsonResponse({
                            'error': 'Profil utilisateur non trouvé. Veuillez compléter votre inscription.'
                        }, status=400)

                # If we get here, we have a valid profile
                login(request, user)
                
                return JsonResponse({
                    'message': 'Login successful',
                    'username': username,
                    'user_type': user_type
                })
                
            else:
                return JsonResponse({
                    'error': 'Identifiants invalides'
                }, status=401)
                
        except json.JSONDecodeError:
            return JsonResponse({
                'error': 'Format de données invalide'
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'error': f'Une erreur est survenue: {str(e)}'
            }, status=500)
            
    return JsonResponse({
        'error': 'Méthode non autorisée'
    }, status=405)
# Login View (for HTML form)

# Registration View
def register(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        if role == 'student':
            return redirect('register_student')
        elif role == 'company':
            return redirect('register_company')
    return render(request, 'register.html')

# Student Registration View
@csrf_exempt
def api_register_student(request):
    if request.method == 'POST':
        print("Received data:", request.POST)
        print("Received files:", request.FILES)
        try:
            # Pour gérer à la fois JSON et FormData
            if request.content_type == 'application/json':
                data = json.loads(request.body)
            else:
                data = request.POST.dict()
                
            # Créer l'utilisateur
            user = User.objects.create_user(
                username=data['username'],
                password=data['password'],
                email=data['email']
            )
            
            # Créer directement le profil étudiant qui hérite de UserProfile
            student = Student.objects.create(
                user=user,  # Lier directement l'utilisateur
                nom=data['lastName'],
                prenom=data['firstName'],
                numero_telephone=data['phoneNumber'],
                etablissement=data['institution'],
                filiere=data['fieldOfStudy'],
                niveau_etude=data['educationLevel'],
                annee_graduation=int(data['graduationYear']),
                type_recherche=data['researchType'],
                date_disponibilite=data['availabilityDate']
            )
            
            # Gérer les fichiers
            if request.FILES:
                if 'cv' in request.FILES:
                    student.cv = request.FILES['cv']
                if 'portfolio' in request.FILES:
                    student.portfolio = request.FILES['portfolio']
                student.save()
            
            return JsonResponse({
                'message': 'Registration successful',
                'username': user.username
            })
            
        except Exception as e:
            # Supprimer l'utilisateur en cas d'erreur pour éviter les utilisateurs orphelins
            if 'user' in locals():
                user.delete()
            return JsonResponse({'error': str(e)}, status=400)
            
    return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def api_register_company(request):
    if request.method == 'POST':
        print("Received company data:", request.POST)
        print("Received files:", request.FILES)
        try:
            # Pour gérer à la fois JSON et FormData
            if request.content_type == 'application/json':
                data = json.loads(request.body)
            else:
                data = request.POST.dict()
                
            # Créer l'utilisateur
            user = User.objects.create_user(
                username=data['username'],
                password=data['password'],
                email=data['email']
            )
            
            # Créer le profil entreprise
            company = Company.objects.create(
                user=user,
                nom_societe=data['companyName'],
                secteur_activite=data['sector'],
                description=data['description'],
                site_web=data['website'],
                numero_telephone=data['phoneNumber'],
                adresse=data['address'],
                taille_entreprise=data['companySize'],
                annee_creation=data['creationYear']
            )
            
            # Gérer le logo
            if request.FILES:
                if 'companyLogo' in request.FILES:
                    company.logo = request.FILES['companyLogo']
                    company.save()
            
            return JsonResponse({
                'message': 'Registration successful',
                'username': user.username
            })
            
        except Exception as e:
            # Supprimer l'utilisateur en cas d'erreur
            if 'user' in locals():
                user.delete()
            return JsonResponse({'error': str(e)}, status=400)
            
    return JsonResponse({'error': 'Method not allowed'}, status=405)

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login_view')

# Edit Profile View
@login_required
def edit_profile(request):
    try:
        user_profile = request.user.profile
    except (Student.DoesNotExist, Company.DoesNotExist):
        return HttpResponseForbidden("Profil introuvable.")

    if hasattr(user_profile, 'student'):
        profile = user_profile.student
        form_class = EditStudentForm
    elif hasattr(user_profile, 'company'):
        profile = user_profile.company
        form_class = EditCompanyForm
    else:
        return HttpResponseForbidden("Type de profil invalide.")

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Les modifications ont été enregistrées avec succès.')
            return redirect('edit_profile')
    else:
        form = form_class(instance=profile)

    return render(request, "edit_profile.html", {"form": form})
