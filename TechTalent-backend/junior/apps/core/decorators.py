# from django.http import HttpResponseForbidden
# from functools import wraps

# # Decorator for checking if the user is a Student
# def student_required(view_func):
#     @wraps(view_func)
#     def _wrapped_view(request, *args, **kwargs):
#         if request.user.role != 'Etudiant':
#             return HttpResponseForbidden("You must be a student to access this page.")
#         return view_func(request, *args, **kwargs)
#     return _wrapped_view

# # Decorator for checking if the user is a Company
# def company_required(view_func):
#     @wraps(view_func)
#     def _wrapped_view(request, *args, **kwargs):
#         if request.user.role != 'Entreprise':
#             return HttpResponseForbidden("You must be a company to access this page.")
#         return view_func(request, *args, **kwargs)
#     return _wrapped_view
