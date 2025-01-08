<!-- src/views/LandingPages/ProfileCandidat.vue -->
<template>
    <div class="page-layout">
      <SidebarCandidat />
      <div class="main-content">
        <div class="container">
          <div class="profile-card">
            <div class="profile-header">
              <img :src="candidat.photo || '/src/assets/img/default-avatar.png'" alt="Photo de profil" class="profile-image"/>
              <h2 class="candidate-name">{{ candidat.firstName }} {{ candidat.lastName }}</h2>
              <p class="candidate-title">{{ candidat.fieldOfStudy }}</p>
            </div>
      
            <div class="profile-sections">
              <div class="profile-section">
                <h3>Informations personnelles</h3>
                <div class="info-grid">
                  <div class="info-item">
                    <label>Nom d'utilisateur</label>
                    <p>{{ candidat.username }}</p>
                  </div>
                  <div class="info-item">
                    <label>Email</label>
                    <p>{{ candidat.email }}</p>
                  </div>
                  <div class="info-item">
                    <label>Téléphone</label>
                    <p>{{ candidat.phoneNumber }}</p>
                  </div>
                </div>
              </div>
      
              <div class="profile-section">
                <h3>Formation</h3>
                <div class="info-grid">
                  <div class="info-item">
                    <label>Établissement</label>
                    <p>{{ candidat.institution }}</p>
                  </div>
                  <div class="info-item">
                    <label>Filière</label>
                    <p>{{ candidat.fieldOfStudy }}</p>
                  </div>
                  <div class="info-item">
                    <label>Niveau d'étude</label>
                    <p>{{ candidat.educationLevel }}</p>
                  </div>
                  <div class="info-item">
                    <label>Année de graduation</label>
                    <p>{{ candidat.graduationYear }}</p>
                  </div>
                </div>
              </div>
      
              <div class="profile-section">
                <h3>Informations professionnelles</h3>
                <div class="info-grid">
                  <div class="info-item">
                    <label>Type de recherche</label>
                    <p>{{ candidat.researchType }}</p>
                  </div>
                  <div class="info-item">
                    <label>Date de disponibilité</label>
                    <p>{{ candidat.availabilityDate }}</p>
                  </div>
                </div>
              </div>
  
              <div class="profile-section">
                <h3>Documents</h3>
                <div class="info-grid">
                  <div class="info-item">
                    <label>CV</label>
                    <a v-if="candidat.cv" :href="candidat.cv" target="_blank" class="document-link">
                      <i class="fas fa-file-pdf"></i> Voir le CV
                    </a>
                  </div>
                  <div class="info-item">
                    <label>Portfolio</label>
                    <a v-if="candidat.portfolio" :href="candidat.portfolio" target="_blank" class="document-link">
                      <i class="fas fa-folder-open"></i> Voir le portfolio
                    </a>
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
  
  const router = useRouter();
  const candidat = ref({
    firstName: "Kenza",
    lastName: "Zahar",
    username: "kenza.zahar",
    email: "kenza.zahar@email.com",
    phoneNumber: "+212 654789321",
    photo: "/src/assets/img/photo_kenza.jpg",
    institution: "ENSA",
    fieldOfStudy: "Génie Informatique",
    educationLevel: "Bac+4",
    graduationYear: "2026",
    researchType: "Stage PFA",
    availabilityDate: "Juillet 2025",
    cv: null,
    portfolio: null
  });
  
  const editProfile = () => {
    router.push('/candidate/dashboard/edit-profile');
  };
  
  onMounted(() => {
    // Ici vous pourrez faire un appel API pour récupérer les informations du candidat
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