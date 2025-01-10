from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from .forms import StudentForm, CompanyForm, EditCompanyForm, CustomUserForm, LoginForm, EditStudentForm
from .models import Company, Student, User, UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Login View
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse("Hey!you have logged in succefully.")
            else:
                msg = 'Identifiants invalides.'
        else:
            msg = 'Erreur lors de la validation du formulaire.'
    return render(request, 'accounts/login.html', {'form': form, 'msg': msg})


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
def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            # Vérifier si le nom d'utilisateur existe déjà
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                messages.error(request, "Ce nom d'utilisateur est déjà pris.")
            else:
                # Créer un utilisateur
                user = User.objects.create_user(
                    username=username,
                    password=form.cleaned_data['password'],
                    email=form.cleaned_data['email']
                )
                
                
                
                # Créer le profil étudiant
                student = form.save(commit=False)
                student.user = user
                if UserProfile.objects.filter(user=user).exists():
                    is_student=True
                student.save()
                print(user)
                print(student)
                messages.success(request, "Inscription réussie. Connectez-vous maintenant.")
                return redirect('login_view')
    else:
        form = StudentForm()

    return render(request, 'register_student.html', {'form': form})


# Company Registration View
def register_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            # Vérifier si le nom d'utilisateur existe déjà
            username = form.cleaned_data['nom_societe']  # Utiliser le nom de la société comme username
            if User.objects.filter(username=username).exists():
                messages.error(request, "Ce nom d'utilisateur est déjà pris.")
            else:
                # Créer un utilisateur
                user = User.objects.create_user(
                    username=username,
                    password=form.cleaned_data['password'],
                    email=form.cleaned_data['email']
                )
                # Créer le profil entreprise
                company = form.save(commit=False)
                company.user = user
                company.save()
                print(user)
                messages.success(request, "Inscription réussie. Connectez-vous maintenant.")
                return redirect('login_view')
    else:
        form = CompanyForm()

    return render(request, 'register_company.html', {'form': form})


# Logout View
def logout_view(request):
    logout(request)
    return redirect('login_view')  # Redirection après déconnexion


# Edit Profile View
@login_required
def edit_profile(request):
    try:
        user_profile = request.user.profile  # Récupérer le profil associé à l'utilisateur
    except (Student.DoesNotExist, Company.DoesNotExist):
        return HttpResponseForbidden("Profil introuvable.")

    # Déterminer le type de profil (étudiant ou entreprise)
    if hasattr(user_profile, 'student'):
        profile = user_profile.student
        form_class = EditStudentForm
    elif hasattr(user_profile, 'company'):
        profile = user_profile.company
        form_class = EditCompanyForm
    else:
        return HttpResponseForbidden("Type de profil invalide.")

    # Gérer la soumission du formulaire
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Les modifications ont été enregistrées avec succès.')
            return redirect('edit_profile')
    else:
        form = form_class(instance=profile)

    return render(request, "edit_profile.html", {"form": form})
