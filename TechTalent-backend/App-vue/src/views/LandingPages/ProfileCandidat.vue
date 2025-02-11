<!-- src/views/LandingPages/ProfileCandidat.vue -->
<template>
  <div class="page-layout">
    <SidebarCandidat />
    <div class="main-content">
      <div class="container">
        <!-- Loading spinner -->
        <div v-if="loading" class="loading-overlay">
          <div class="loading-spinner">Chargement...</div>
        </div>

        <!-- Error message -->
        <div v-if="error" class="error-message">
          {{ error }}
          <button @click="loadProfileData" class="retry-button">
            Réessayer
          </button>
        </div>

        <!-- Profile content -->
        <div v-if="!loading && !error && candidat" class="profile-card">
          <div class="profile-header">
            <img 
              :src="getImageUrl(candidat.photo_profil)" 
              :alt="`Photo de ${candidat.firstName}`" 
              class="profile-image"
              @load="handleImageLoad"
              @error="handleImageError"
            />

            <h2 class="candidate-name">
              {{ candidat.firstName }} {{ candidat.lastName }}
            </h2>
            <p class="candidate-title">{{ candidat.fieldOfStudy }}</p>
          </div>

          <div class="profile-sections">
            <!-- Personal Information -->
            <div class="profile-section">
              <h3>Informations personnelles</h3>
              <div class="info-grid">
                <div v-if="candidat.username" class="info-item">
                  <label>Nom d'utilisateur</label>
                  <p>{{ candidat.username }}</p>
                </div>
                <div v-if="candidat.email" class="info-item">
                  <label>Email</label>
                  <p>{{ candidat.email }}</p>
                </div>
                <div v-if="candidat.phoneNumber" class="info-item">
                  <label>Téléphone</label>
                  <p>{{ candidat.phoneNumber }}</p>
                </div>
              </div>
            </div>

            <!-- Education -->
            <div class="profile-section">
              <h3>Formation</h3>
              <div class="info-grid">
                <div v-if="candidat.institution" class="info-item">
                  <label>Établissement</label>
                  <p>{{ candidat.institution }}</p>
                </div>
                <div v-if="candidat.fieldOfStudy" class="info-item">
                  <label>Filière</label>
                  <p>{{ candidat.fieldOfStudy }}</p>
                </div>
                <div v-if="candidat.educationLevel" class="info-item">
                  <label>Niveau d'étude</label>
                  <p>{{ candidat.educationLevel }}</p>
                </div>
                <div v-if="candidat.graduationYear" class="info-item">
                  <label>Année de graduation</label>
                  <p>{{ candidat.graduationYear }}</p>
                </div>
              </div>
            </div>

            <!-- Professional Information -->
            <div class="profile-section">
              <h3>Informations professionnelles</h3>
              <div class="info-grid">
                <div v-if="candidat.researchType" class="info-item">
                  <label>Type de recherche</label>
                  <p>{{ candidat.researchType }}</p>
                </div>
                <div v-if="candidat.availabilityDate" class="info-item">
                  <label>Date de disponibilité</label>
                  <p>{{ formatDate(candidat.availabilityDate) }}</p>
                </div>
              </div>
            </div>

            <!-- Documents -->
            <div class="profile-section">
              <h3>Documents</h3>
              <div class="info-grid">
                <div class="info-item">
                  <label>CV</label>
                  <a 
                    v-if="candidat.cv" 
                    :href="getDocumentUrl(candidat.cv)" 
                    target="_blank" 
                    class="document-link"
                  >
                    <i class="fas fa-file-pdf"></i> Voir le CV
                  </a>
                  <p v-else class="no-document">Aucun CV téléchargé</p>
                </div>
                <div class="info-item">
                  <label>Portfolio</label>
                  <a 
                    v-if="candidat.portfolio" 
                    :href="getDocumentUrl(candidat.portfolio)" 
                    target="_blank" 
                    class="document-link"
                  >
                    <i class="fas fa-folder-open"></i> Voir le portfolio
                  </a>
                  <p v-else class="no-document">Aucun portfolio téléchargé</p>
                </div>
              </div>
            </div>
          </div>

          <div class="profile-actions">
            <button @click="editProfile" class="edit-button">
              <i class="fas fa-edit"></i> Modifier le profil
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import SidebarCandidat from './components/SidebarCandidat.vue';
import { getProfile } from '@/apiClient';

const API_URL = 'http://localhost:8000';
const DEFAULT_AVATAR = '/src/assets/img/default-avatar.png';

const router = useRouter();
const loading = ref(true);
const error = ref(null);
const candidat = ref({
  firstName: "",
  lastName: "",
  username: "",
  email: "",
  phoneNumber: "",
  photo_profil: null,
  institution: "",
  fieldOfStudy: "",
  educationLevel: "",
  graduationYear: "",
  researchType: "",
  availabilityDate: "",
  cv: null,
  portfolio: null
});

// Helper functions restent les mêmes...

// Remplacez la fonction loadProfileData existante par la nouvelle version
const loadProfileData = async () => {
  try {
    loading.value = true;
    error.value = null;
    console.log('Début du chargement du profil...');
    
    const response = await getProfile();
    console.log('Réponse reçue:', response);
    
    if (!response) {
      console.error('Pas de réponse reçue');
      throw new Error('Aucune donnée reçue du serveur');
    }

    console.log('Mise à jour du candidat avec:', response);
    candidat.value = {
      ...candidat.value,
      ...response,
    };
    console.log('Candidat mis à jour:', candidat.value);
    
  } catch (err) {
    console.error('Erreur détaillée:', err);
    console.error('Message d\'erreur:', err.message);
    console.error('Réponse d\'erreur:', err.response);
    error.value = err.message || "Impossible de charger les données du profil";
    if (err.message.includes('401')) {
      console.log('Redirection vers login due à 401');
      router.push('/login');
    }
  } finally {
    loading.value = false;
    console.log('Chargement terminé');
  }
};

const editProfile = () => {
  router.push('/edit-profile');
};

const formatDate = (date) => {
  if (!date) return '';
  return new Date(date).toLocaleDateString('fr-FR');
};

const getImageUrl = (photoUrl) => {
  return photoUrl;
};


const getDocumentUrl = (documentUrl) => {
  return documentUrl;
};
const isImageLoaded = ref(false);

const handleImageLoad = () => {
  isImageLoaded.value = true;
};

const handleImageError = (event) => {
  event.target.src = DEFAULT_AVATAR;
};


onMounted(() => {
  loadProfileData();
});
</script>
      
<style scoped>
  .page-layout {
    display: flex;
    min-height: 100vh;
  }
  
  .main-content {
    flex: 1;
    margin-left: 260px;
    padding: 2rem;
    background: #f9fafb;
    min-height: 100vh;
  }
  
  .container {
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .profile-card {
    background: white;
    border-radius: 0.5rem;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    padding: 2rem;
  }
  
  .profile-header {
    text-align: center;
    margin-bottom: 2rem;
  }
  
  .profile-image {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    object-fit: cover;
    margin-bottom: 1rem;
  }
  
  .candidate-name {
    font-size: 1.5rem;
    color: #111827;
    margin: 0;
  }
  
  .candidate-title {
    color: #6b7280;
    margin-top: 0.5rem;
  }
  
  .profile-sections {
    display: grid;
    gap: 2rem;
  }
  
  .profile-section {
    border-bottom: 1px solid #e5e7eb;
    padding-bottom: 1.5rem;
  }
  
  .profile-section h3 {
    color: #4b5563;
    margin-bottom: 1rem;
  }
  
  .info-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
  }
  
  .info-item label {
    font-size: 0.875rem;
    color: #6b7280;
    display: block;
    margin-bottom: 0.5rem;
  }
  
  .info-item p {
    color: #111827;
    margin: 0;
  }
  
  .document-link {
    color: #5d6c8d;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
  }
  
  .document-link:hover {
    text-decoration: underline;
  }
  
  .profile-actions {
    margin-top: 2rem;
    display: flex;
    justify-content: flex-end;
  }
  
  .edit-button {
    background: #5d6c8d;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 0.375rem;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }
  
  .edit-button:hover {
    background: #4a5578;
  }
</style>