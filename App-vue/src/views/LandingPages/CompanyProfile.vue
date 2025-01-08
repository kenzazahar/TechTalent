<!-- src/views/LandingPages/CompanyProfile.vue -->
<template>
    <div class="page-layout">
      <Sidebar />
      <div class="main-content">
        <div class="container">
          <div class="profile-card">
            <div class="profile-header">
              <img :src="company.logo" alt="Logo entreprise" class="company-logo"/>
              <h2 class="company-name">{{ company.companyName }}</h2>
            </div>
    
            <div class="profile-sections">
              <div class="profile-section">
                <h3>Informations générales</h3>
                <div class="info-grid">
                  <div class="info-item">
                    <label>Secteur d'activité</label>
                    <p>{{ company.sector }}</p>
                  </div>
                  <div class="info-item">
                    <label>Taille de l'entreprise</label>
                    <p>{{ company.companySize }}</p>
                  </div>
                  <div class="info-item">
                    <label>Année de création</label>
                    <p>{{ company.creationYear }}</p>
                  </div>
                </div>
              </div>
    
              <div class="profile-section">
                <h3>Description</h3>
                <p class="description">{{ company.description }}</p>
              </div>
    
              <div class="profile-section">
                <h3>Contact</h3>
                <div class="info-grid">
                  <div class="info-item">
                    <label>Site Web</label>
                    <a :href="company.website" target="_blank">{{ company.website }}</a>
                  </div>
                  <div class="info-item">
                    <label>Téléphone</label>
                    <p>{{ company.phoneNumber }}</p>
                  </div>
                  <div class="info-item">
                    <label>Adresse</label>
                    <p>{{ company.address }}</p>
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
  import Sidebar from './components/Sidebar.vue'
  
  const router = useRouter();
  const company = ref({
    companyName: "TechCorp",
    logo: "/src/assets/img/logo1.jpg",
    sector: "Technologies de l'information",
    companySize: "50-100 employés",
    creationYear: "2020",
    description: "TechCorp est une entreprise innovante spécialisée dans le Dev Web...",
    website: "www.techcorp.ma",
    phoneNumber: "+212 576548221",
    address: "Casablanca, Maroc"
  });
  
  const editProfile = () => {
    router.push('/company/edit-profile');
  };
  
  onMounted(() => {
    // Ici vous pourrez faire un appel API pour récupérer les informations de l'entreprise
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
  
  .company-logo {
    width: 120px;
    height: 120px;
    object-fit: contain;
    margin-bottom: 1rem;
  }
  
  .company-name {
    font-size: 1.5rem;
    color: #111827;
    margin: 0;
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
  
  .info-item p, .info-item a {
    color: #111827;
    margin: 0;
  }
  
  .description {
    line-height: 1.6;
    color: #374151;
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