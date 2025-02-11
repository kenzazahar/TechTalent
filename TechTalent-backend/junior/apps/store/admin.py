from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Skill)
admin.site.register(JobOffer)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')  # Columns to display in the admin list view
    prepopulated_fields = {'slug': ('title',)}  # Automatically populate the slug field based on the title
