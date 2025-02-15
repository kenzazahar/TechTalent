# Generated by Django 5.1.6 on 2025-02-15 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_userprofile_is_company_userprofile_is_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('short_description', models.CharField(max_length=500)),
                ('details', models.TextField()),
                ('full_description', models.TextField()),
                ('required_skills', models.TextField()),
                ('contract_type', models.CharField(max_length=100)),
                ('work_mode', models.CharField(max_length=100)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('offer_duration', models.CharField(blank=True, max_length=100, null=True)),
                ('salary', models.CharField(blank=True, max_length=100, null=True)),
                ('recruiter_name', models.CharField(max_length=255)),
                ('recruiter_email', models.EmailField(max_length=254)),
                ('recruiter_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('offer_image', models.ImageField(blank=True, null=True, upload_to='job_offers/')),
                ('status', models.CharField(choices=[('draft', 'Brouillon'), ('published', 'Publié')], default='draft', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_offers_core', to='core.company')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
