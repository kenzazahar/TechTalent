from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from .models import *
from apps.core.models import *
from .forms import * # We'll define this form next
#from apps.core.decorators import student_required, company_required
from django.shortcuts import get_object_or_404
from apps.core.templates import *
# Create your views here.
def display_jobs(request):
    jobs = JobOffer.objects.all()
    context = {
        'jobs': jobs
    } 
    return render(request,'display_jobs.html',context)

@login_required
def add_job_offer(request):
    # Ensure the logged-in user is associated with a company
    try:
        company = Company.objects.get(user=request.user)
        print(f"User: {request.user}")
        print(f"Company: {company}")
    except Company.DoesNotExist:
        return HttpResponseForbidden("You must be associated with a company to add a job offer.")

    # Prevent modification of existing job offers
    if request.method == 'POST' and 'job_offer_id' in request.POST:
        return HttpResponseForbidden("Job offers cannot be modified once created.")

    if request.method == 'POST':
        form = JobOfferForm(request.POST)
        if form.is_valid():
            try:
                job_offer = form.save(commit=False)
                job_offer.company = company  # Assign the company
                job_offer.save()
                form.save_m2m()  # Save many-to-many relationships
                return redirect('job_offer_list')
            except Exception as e:
                # Log the error for debugging
                print(f"Error saving job offer: {e}")
                return HttpResponse("An error occurred while saving the job offer.")
        else:
            print("Form errors:", form.errors)

    else:
        form = JobOfferForm()

    return render(request, 'company/add_job_offer.html', {'form': form})

@login_required
#@company_required
def job_offer_list(request):
    # Ensure the user is authenticated
    if not request.user.is_authenticated:
        return HttpResponseForbidden("You must be logged in to view job offers.")
    print(f"User: {request.user}")
    try:
        # Check if the logged-in user is associated with a company
        company = Company.objects.get(user=request.user)
        print(f"Company: {company}")
    except Company.DoesNotExist:
        return HttpResponseForbidden("Only companies can view their job offers.")

    # Get job offers posted by the logged-in company
    job_offers = JobOffer.objects.filter(company=company)
    return render(request, 'company/job_offer_list.html', {'job_offers': job_offers})

@login_required
def List_AllJobs(request):
    # Ensure the user is authenticated
    if not request.user.is_authenticated:
        return HttpResponseForbidden("You must be logged in to view job offers.")
    else:    
        print(f"User: {request.user}")
        # Get job offers posted by the logged-in company
        job_offers = JobOffer.objects.all() 
        return render(request, 'company/job_offer_list.html', {'job_offers': job_offers})

@login_required
def search_bar(request):
    search_query = request.GET.get('q', '')  # Search query
    selected_category = request.GET.get('category', '')
    selected_skill = request.GET.get('skill', '')
    selected_job_type = request.GET.get('job_type', '')

    # Base queryset
    results = JobOffer.objects.all()

    # Apply search query filter
    if search_query:
        results = JobOffer.objects.filter(
            title__icontains=search_query
        ) | JobOffer.objects.filter(
            slug__icontains=search_query
        ) | JobOffer.objects.filter(
            skills__name__icontains=search_query
        ) | JobOffer.objects.filter(
            category__title__icontains=search_query
        ) | JobOffer.objects.filter(
            company__nom_societe__icontains=search_query  # Ensure to use the actual field name in the related model
        )

    # Apply filters based on selected options
    if selected_category:
        results = results.filter(category__id=selected_category)
    if selected_skill:
        results = results.filter(skills__id=selected_skill)
    if selected_job_type:
        results = results.filter(job_type=selected_job_type)

    # Fetch filter options
    categories = Category.objects.all()
    skills = Skill.objects.all()
    job_types = JobOffer.JOB_TYPE_CHOICES

    context = {
        'results': results.distinct(),  # Ensure no duplicates when using OR queries
        'search_query': search_query,
        'categories': categories,
        'skills': skills,
        'job_types': job_types,
        'selected_category': selected_category,
        'selected_skill': selected_skill,
        'selected_job_type': selected_job_type,
    }
    return render(request, 'search/search_bar.html', context)

@login_required
def job_detail(request, job_id):
    job = get_object_or_404(JobOffer, id=job_id)
    return render(request, 'search/job_detail.html', {'job': job})

@login_required
def apply_to_job(request, job_id):
    job = get_object_or_404(JobOffer, id=job_id)
    user_profile = request.user.profile

    # Check if the student has already applied
    if JobApplication.objects.filter(student=user_profile.student, job_offer=job).exists():
        if hasattr(user_profile, 'student'):  # Ensure the user is a student
            return HttpResponseForbidden("You have already applied for this job.")
        else:
            return HttpResponse("Not working yet.")

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user_profile = user_profile  # Associate with the logged-in user's profile
            application.student = user_profile.student
            application.job_offer = job
            application.save()
            return redirect('job_detail', job_id=job.id)
    else:
        form = JobApplicationForm()

    return render(request, 'job_application.html', {'job': job, 'form': form})
