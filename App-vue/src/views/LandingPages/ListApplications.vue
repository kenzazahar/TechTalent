<!-- MyApplications.vue -->
<template>
    <div class="layout">
      <Sidebar />
      <div class="main-content">
        <div class="applications-dashboard">
          <!-- En-tête avec stats -->
          <div class="stats-grid">
            <div class="stat-card">
              <i class="fas fa-paper-plane stat-icon"></i>
              <div class="stat-info">
                <span class="stat-value">{{ totalApplications }}</span>
                <span class="stat-label">Candidatures totales</span>
              </div>
            </div>
            <div class="stat-card">
              <i class="fas fa-clock stat-icon"></i>
              <div class="stat-info">
                <span class="stat-value">{{ pendingApplications }}</span>
                <span class="stat-label">En attente</span>
              </div>
            </div>
            <div class="stat-card">
              <i class="fas fa-check-circle stat-icon"></i>
              <div class="stat-info">
                <span class="stat-value">{{ acceptedApplications }}</span>
                <span class="stat-label">Acceptées</span>
              </div>
            </div>
            <div class="stat-card">
              <i class="fas fa-times-circle stat-icon"></i>
              <div class="stat-info">
                <span class="stat-value">{{ rejectedApplications }}</span>
                <span class="stat-label">Refusées</span>
              </div>
            </div>
          </div>
  
          <!-- Filtres -->
          <div class="filters-section">
            <div class="search-bar">
              <i class="fas fa-search search-icon"></i>
              <input 
                type="text" 
                v-model="searchQuery"
                placeholder="Rechercher une candidature..." 
                class="search-input"
              />
            </div>
            <div class="filter-buttons">
              <button 
                v-for="status in ['Toutes', 'En attente', 'Entretien', 'Acceptée', 'Refusée']"
                :key="status"
                :class="['filter-btn', { active: currentStatus === status }]"
                @click="currentStatus = status"
              >
                {{ status }}
              </button>
            </div>
          </div>
  
          <!-- Liste des candidatures -->
          <div class="applications-list">
            <div v-for="application in filteredApplications" 
                 :key="application.id" 
                 class="application-card"
            >
              <div class="company-info">
                <img :src="application.companyLogo" :alt="application.companyName" class="company-logo"/>
                <div>
                  <h3 class="job-title">{{ application.jobTitle }}</h3>
                  <p class="company-name">{{ application.companyName }}</p>
                </div>
              </div>
  
              <div class="application-details">
                <div class="detail-item">
                  <i class="fas fa-calendar"></i>
                  <span>Postulé le {{ formatDate(application.applicationDate) }}</span>
                </div>
                <div class="detail-item">
                  <i class="fas fa-map-marker-alt"></i>
                  <span>{{ application.location }}</span>
                </div>
              </div>
  
              <div class="application-status">
                <span :class="['status-badge', application.status.toLowerCase()]">
                  {{ application.status }}
                </span>
              </div>
  
              <div class="application-actions">
                <button class="action-btn view-btn" @click="viewApplication(application.id)">
                  <i class="fas fa-eye"></i>
                  Voir détails
                </button>
                <button v-if="application.status === 'En attente'" 
                        class="action-btn withdraw-btn"
                        @click="withdrawApplication(application.id)"
                >
                  <i class="fas fa-times"></i>
                  Retirer
                </button>
              </div>
            </div>
          </div>
  
          <!-- Message si aucune candidature -->
          <div v-if="filteredApplications.length === 0" class="no-applications">
            <i class="fas fa-folder-open no-data-icon"></i>
            <p>Aucune candidature ne correspond à vos critères</p>
            <button class="browse-jobs-btn" @click="$router.push('/candidate/dashboard/offers')">
              Parcourir les offres
            </button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue';
  import { useRouter } from 'vue-router';
  import Sidebar from './components/Sidebar.vue';
  
  const router = useRouter();
  const searchQuery = ref('');
  const currentStatus = ref('Toutes');
  
  // Données simulées
  const applications = ref([
    {
      id: 1,
      jobTitle: 'Développeur Full Stack',
      companyName: 'TechCorp',
      companyLogo: '/src/assets/img/company1.png',
      applicationDate: '2024-01-15',
      location: 'Casablanca',
      status: 'En attente'
    },
    {
      id: 2,
      jobTitle: 'UX Designer',
      companyName: 'DesignStudio',
      companyLogo: '/src/assets/img/company2.png',
      applicationDate: '2024-01-10',
      location: 'Rabat',
      status: 'Entretien'
    },
    {
      id: 3,
      jobTitle: 'Product Manager',
      companyName: 'InnovTech',
      companyLogo: '/src/assets/img/company3.png',
      applicationDate: '2024-01-05',
      location: 'Tanger',
      status: 'Acceptée'
    }
  ]);
  
  // Statistiques calculées
  const totalApplications = computed(() => applications.value.length);
  const pendingApplications = computed(() => 
    applications.value.filter(app => app.status === 'En attente').length
  );
  const acceptedApplications = computed(() => 
    applications.value.filter(app => app.status === 'Acceptée').length
  );
  const rejectedApplications = computed(() => 
    applications.value.filter(app => app.status === 'Refusée').length
  );
  
  // Filtrage des candidatures
  const filteredApplications = computed(() => {
    return applications.value.filter(app => {
      const matchesSearch = app.jobTitle.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
                           app.companyName.toLowerCase().includes(searchQuery.value.toLowerCase());
      const matchesStatus = currentStatus.value === 'Toutes' || app.status === currentStatus.value;
      return matchesSearch && matchesStatus;
    });
  });
  
  // Fonctions
  const formatDate = (date) => {
    return new Date(date).toLocaleDateString('fr-FR', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  };
  
  const viewApplication = (id) => {
    router.push(`/candidate/dashboard/applications/${id}`);
  };
  
  const withdrawApplication = (id) => {
    if (confirm('Êtes-vous sûr de vouloir retirer cette candidature ?')) {
      applications.value = applications.value.filter(app => app.id !== id);
    }
  };
  </script>
  
  <style scoped>
  .layout {
    display: flex;
  }
  
  .main-content {
    flex: 1;
    margin-left: 260px;
    padding: 2rem;
  }
  
  .applications-dashboard {
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin-bottom: 2rem;
  }
  
  .stat-card {
    background: white;
    padding: 1.5rem;
    border-radius: 0.5rem;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    display: flex;
    align-items: center;
    gap: 1rem;
  }
  
  .stat-icon {
    font-size: 1.5rem;
    color: #34343d;
    background: rgba(52, 52, 61, 0.1);
    padding: 1rem;
    border-radius: 0.5rem;
  }
  
  .stat-info {
    display: flex;
    flex-direction: column;
  }
  
  .stat-value {
    font-size: 1.5rem;
    font-weight: 600;
    color: #34343d;
  }
  
  .stat-label {
    font-size: 0.875rem;
    color: #6b7280;
  }
  
  .filters-section {
    margin-bottom: 2rem;
  }
  
  .search-bar {
    position: relative;
    margin-bottom: 1rem;
  }
  
  .search-input {
    width: 100%;
    padding: 0.75rem 1rem 0.75rem 2.5rem;
    border: 1px solid #e5e7eb;
    border-radius: 0.375rem;
    outline: none;
    font-size: 1rem;
  }
  
  .search-icon {
    position: absolute;
    left: 0.75rem;
    top: 50%;
    transform: translateY(-50%);
    color: #9ca3af;
  }
  
  .filter-buttons {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
  }
  
  .filter-btn {
    padding: 0.5rem 1rem;
    border: 1px solid #e5e7eb;
    border-radius: 0.375rem;
    background: white;
    color: #6b7280;
    cursor: pointer;
    transition: all 0.2s;
  }
  
  .filter-btn.active {
    background: #34343d;
    color: white;
    border-color: #34343d;
  }
  
  .application-card {
    background: white;
    border-radius: 0.5rem;
    padding: 1.5rem;
    margin-bottom: 1rem;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    display: grid;
    grid-template-columns: 2fr 2fr 1fr 1fr;
    align-items: center;
    gap: 1.5rem;
  }
  
  .company-info {
    display: flex;
    align-items: center;
    gap: 1rem;
  }
  
  .company-logo {
    width: 50px;
    height: 50px;
    object-fit: cover;
    border-radius: 0.375rem;
  }
  
  .job-title {
    font-size: 1.125rem;
    font-weight: 600;
    color: #34343d;
    margin: 0;
  }
  
  .company-name {
    font-size: 0.875rem;
    color: #6b7280;
    margin: 0.25rem 0 0 0;
  }
  
  .application-details {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .detail-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: #6b7280;
    font-size: 0.875rem;
  }
  
  .status-badge {
    padding: 0.25rem 0.75rem;
    border-radius: 1rem;
    font-size: 0.875rem;
    font-weight: 500;
  }
  
  .status-badge.en-attente {
    background: #FEF3C7;
    color: #D97706;
  }
  
  .status-badge.entretien {
    background: #DBEAFE;
    color: #2563EB;
  }
  
  .status-badge.acceptée {
    background: #D1FAE5;
    color: #059669;
  }
  
  .status-badge.refusée {
    background: #FEE2E2;
    color: #DC2626;
  }
  
  .application-actions {
    display: flex;
    gap: 0.5rem;
  }
  
  .action-btn {
    padding: 0.5rem 1rem;
    border-radius: 0.375rem;
    font-size: 0.875rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    cursor: pointer;
    transition: all 0.2s;
  }
  
  .view-btn {
    background: #34343d;
    color: white;
    border: none;
  }
  
  .view-btn:hover {
    background: #1f1f24;
  }
  
  .withdraw-btn {
    background: white;
    color: #DC2626;
    border: 1px solid #DC2626;
  }
  
  .withdraw-btn:hover {
    background: #FEE2E2;
  }
  
  .no-applications {
    text-align: center;
    padding: 3rem;
    color: #6b7280;
  }
  
  .no-data-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
    color: #9ca3af;
  }
  
  .browse-jobs-btn {
    margin-top: 1rem;
    padding: 0.75rem 1.5rem;
    background: #34343d;
    color: white;
    border: none;
    border-radius: 0.375rem;
    cursor: pointer;
    transition: background-color 0.2s;
  }
  
  .browse-jobs-btn:hover {
    background: #1f1f24;
  }
  </style>