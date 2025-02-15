from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from .forms import StudentForm, CompanyForm, EditCompanyForm, CustomUserForm, LoginForm, EditStudentForm
from .models import Company, Student, User, UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from .models import JobOffer
from django.core.files.base import ContentFile
import base64

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
                if 'photo' in request.FILES:
                    student.photo = request.FILES['photo']
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


@require_http_methods(["GET", "OPTIONS"])
@csrf_exempt
@login_required
def api_get_profile(request):
    # Gérer les requêtes OPTIONS pour CORS
    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, X-CSRFToken"
        response["Access-Control-Allow-Origin"] = "http://localhost:5173"
        response["Access-Control-Allow-Credentials"] = "true"
        return response

    # Vérifier l'authentification
    if not request.user.is_authenticated:
        print("Utilisateur non authentifié")
        return JsonResponse(
            {'error': 'Utilisateur non authentifié'}, 
            status=401
        )

    try:
        print(f"Recherche du profil pour l'utilisateur: {request.user.username}")
        student = Student.objects.get(user=request.user)
        print("Profil étudiant trouvé")

        def get_file_url(file_field):
            try:
                if file_field and hasattr(file_field, 'url'):
                    return request.build_absolute_uri(file_field.url)
                return None
            except Exception as e:
                print(f"Erreur lors de la récupération de l'URL du fichier: {e}")
                return None

        # Préparer les données du profil
        data = {
            'username': request.user.username,
            'email': request.user.email,
            'firstName': student.prenom,
            'lastName': student.nom,
            'phoneNumber': student.numero_telephone,
            'institution': student.etablissement,
            'fieldOfStudy': student.filiere,
            'educationLevel': student.niveau_etude,
            'graduationYear': student.annee_graduation,
            'researchType': student.type_recherche,
            'availabilityDate': student.date_disponibilite,
            'cv': get_file_url(student.cv),
            'portfolio': get_file_url(student.portfolio),
            'photo_profil': get_file_url(student.photo_profil) if hasattr(student, 'photo_profil') else None,
            'userType': 'student'
        }

        print("Données préparées:", data)
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "http://localhost:5173"
        response["Access-Control-Allow-Credentials"] = "true"
        return response

    except Student.DoesNotExist:
        print("Profil étudiant non trouvé")
        return JsonResponse(
            {'error': 'Profil étudiant non trouvé'}, 
            status=404
        )
    except Exception as e:
        print(f"Erreur inattendue: {str(e)}")
        return JsonResponse(
            {'error': str(e)}, 
            status=500
        )


@require_http_methods(["GET", "OPTIONS"])
@csrf_exempt
@login_required
def api_get_company_profile(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Utilisateur non authentifié'}, status=401)

    try:
        company = Company.objects.get(user=request.user)
        
        # Correspondance exacte avec les noms des champs du modèle
        data = {
            'companyName': company.nom_societe,
            'companyLogo': request.build_absolute_uri(company.logo_societe.url) if company.logo_societe else None,
            'sector': company.secteur_activite,
            'description': company.description,
            'website': company.site_web,
            'phoneNumber': company.numero_telephone,
            'address': company.adresse,
            'companySize': company.taille_entreprise,
            'creationYear': company.annee_creation
        }
        
        return JsonResponse(data)

    except Company.DoesNotExist:
        return JsonResponse({'error': 'Profil entreprise non trouvé'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["POST", "OPTIONS"])
@csrf_exempt
@login_required
def api_update_profile(request):
    try:
        data = request.POST.dict()
        files = request.FILES

        # Vérifier si l'utilisateur est un étudiant ou une entreprise
        profile = None
        if Student.objects.filter(user=request.user).exists():
            profile = Student.objects.get(user=request.user)
            # Mise à jour des champs pour l'étudiant
            profile.prenom = data.get('firstName', profile.prenom)
            profile.nom = data.get('lastName', profile.nom)
            profile.numero_telephone = data.get('phoneNumber', profile.numero_telephone)
            profile.etablissement = data.get('institution', profile.etablissement)
            profile.filiere = data.get('fieldOfStudy', profile.filiere)
            profile.niveau_etude = data.get('educationLevel', profile.niveau_etude)
            profile.annee_graduation = data.get('graduationYear', profile.annee_graduation)
            profile.type_recherche = data.get('researchType', profile.type_recherche)
            profile.date_disponibilite = data.get('availabilityDate', profile.date_disponibilite)

            # Gestion des fichiers
            if 'cv' in files:
                profile.cv = files['cv']
            if 'portfolio' in files:
                profile.portfolio = files['portfolio']
            if 'photo_profil' in files:
                profile.photo_profil = files['photo_profil']

        elif Company.objects.filter(user=request.user).exists():
            profile = Company.objects.get(user=request.user)
            # Mise à jour des champs pour l'entreprise
            profile.nom_societe = data.get('companyName', profile.nom_societe)
            profile.secteur_activite = data.get('sector', profile.secteur_activite)
            profile.description = data.get('description', profile.description)
            profile.site_web = data.get('website', profile.site_web)
            profile.numero_telephone = data.get('phoneNumber', profile.numero_telephone)
            profile.adresse = data.get('address', profile.adresse)
            profile.taille_entreprise = data.get('companySize', profile.taille_entreprise)
            profile.annee_creation = data.get('creationYear', profile.annee_creation)

            if 'logo' in files:
                profile.logo = files['logo']

        else:
            return JsonResponse({'error': 'Utilisateur non reconnu'}, status=404)

        profile.save()
        return JsonResponse({'message': 'Profil mis à jour avec succès'})

    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Profil introuvable'}, status=404)
    except Exception as e:
        return JsonResponse({'error': f'Erreur lors de la mise à jour : {str(e)}'}, status=400)


@require_http_methods(["POST", "OPTIONS"])
@csrf_exempt
@login_required
def api_update_company_profile(request):
    try:
        data = request.POST.dict()
        files = request.FILES
        
        company = Company.objects.get(user=request.user)
        
        # Mise à jour des champs
        company.nom_societe = data.get('companyName', company.nom_societe)
        company.secteur_activite = data.get('sector', company.secteur_activite)
        company.description = data.get('description', company.description)
        company.site_web = data.get('website', company.site_web)
        company.numero_telephone = data.get('phoneNumber', company.numero_telephone)
        company.adresse = data.get('address', company.adresse)
        company.taille_entreprise = data.get('companySize', company.taille_entreprise)
        company.annee_creation = data.get('creationYear', company.annee_creation)

        if 'companyLogo' in files:
            company.logo_societe = files['companyLogo']

        company.save()
        return JsonResponse({'message': 'Profil mis à jour avec succès'})

    except Company.DoesNotExist:
        return JsonResponse({'error': 'Profil entreprise non trouvé'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@require_http_methods(["POST", "OPTIONS"])
@csrf_exempt
@login_required
def api_create_job_offer(request):
    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, X-CSRFToken"
        return response

    try:
        # Vérifier si l'utilisateur est une entreprise
        if not hasattr(request.user.profile, 'company'):
            return JsonResponse({'error': 'Seules les entreprises peuvent créer des offres'}, status=403)

        data = request.POST.dict() if request.POST else json.loads(request.body)
        
        # Créer l'offre
        job_offer = JobOffer(
            company=request.user.profile.company,
            title=data.get('title'),
            short_description=data.get('shortDescription'),
            details=data.get('details'),
            full_description=data.get('fullDescription'),
            required_skills=data.get('requiredSkills'),
            contract_type=data.get('contractType'),
            work_mode=data.get('workMode'),
            location=data.get('location'),
            offer_duration=data.get('offerDuration'),
            salary=data.get('salary'),
            recruiter_name=data.get('recruiterName'),
            recruiter_email=data.get('recruiterEmail'),
            recruiter_phone=data.get('recruiterPhone'),
            status='published' if data.get('isPublish') else 'draft'  # Assurez-vous que le statut est correctement défini
        )

        # Gérer l'image de l'offre si présente
        if 'offerImage' in request.FILES:
            job_offer.offer_image = request.FILES['offerImage']

        job_offer.save()
        
        return JsonResponse({
            'message': 'Offre créée avec succès',
            'id': job_offer.id
        })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

# Vue pour récupérer les offres publiées
@require_http_methods(["GET"])
@csrf_exempt
@login_required
def api_get_published_offers(request):
    try:
        company = request.user.profile.company
        offers = JobOffer.objects.filter(company=company, status='published')
        
        offers_data = [{
            'id': offer.id,
            'title': offer.title,
            'location': offer.location,
            'image': request.build_absolute_uri(offer.offer_image.url) if offer.offer_image else None,
            'shortDescription': offer.short_description,
            'contractType': offer.contract_type,
            'workMode': offer.work_mode,
            'created_at': offer.created_at
        } for offer in offers]
        
        return JsonResponse({'offers': offers_data})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

# Vue pour récupérer les brouillons
@require_http_methods(["GET"])
@csrf_exempt
@login_required
def api_get_draft_offers(request):
    try:
        company = request.user.profile.company
        offers = JobOffer.objects.filter(company=company, status='draft')
        
        offers_data = [{
            'id': offer.id,
            'title': offer.title,
            'location': offer.location,
            'image': request.build_absolute_uri(offer.offer_image.url) if offer.offer_image else None,
            'shortDescription': offer.short_description,
            'contractType': offer.contract_type,
            'workMode': offer.work_mode,
            'created_at': offer.created_at
        } for offer in offers]
        
        return JsonResponse({'offers': offers_data})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

# Vue pour mettre à jour une offre
@require_http_methods(["PUT", "POST", "OPTIONS"])
@csrf_exempt
@login_required
def api_update_job_offer(request, offer_id):
    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Methods"] = "PUT, POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, X-CSRFToken"
        return response

    try:
        offer = JobOffer.objects.get(id=offer_id, company=request.user.profile.company)
        data = request.POST.dict() if request.POST else json.loads(request.body)

        # Mettre à jour les champs
        fields_to_update = [
            'title', 'short_description', 'details', 'full_description',
            'required_skills', 'contract_type', 'work_mode', 'location',
            'offer_duration', 'salary', 'recruiter_name', 'recruiter_email',
            'recruiter_phone'
        ]
        
        for field in fields_to_update:
            if field in data:
                setattr(offer, field, data[field])

        # Mettre à jour le statut si spécifié
        if 'isPublish' in data:
            offer.status = 'published' if data['isPublish'] else 'draft'

        # Gérer l'image si présente
        if 'offerImage' in request.FILES:
            offer.offer_image = request.FILES['offerImage']

        offer.save()
        
        return JsonResponse({'message': 'Offre mise à jour avec succès'})

    except JobOffer.DoesNotExist:
        return JsonResponse({'error': 'Offre non trouvée'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    