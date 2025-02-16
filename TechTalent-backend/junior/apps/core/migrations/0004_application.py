# Generated by Django 5.1.6 on 2025-02-16 18:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_joboffer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'En attente'), ('reviewing', "En cours d'examen"), ('interviewed', 'Entretien effectué'), ('accepted', 'Acceptée'), ('rejected', 'Refusée')], default='pending', max_length=20)),
                ('cv', models.FileField(upload_to='applications/cv/')),
                ('cover_letter', models.FileField(blank=True, null=True, upload_to='applications/cover_letters/')),
                ('message', models.TextField(blank=True, null=True)),
                ('job_offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='core.joboffer')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='core.student')),
            ],
            options={
                'ordering': ['-application_date'],
            },
        ),
    ]
