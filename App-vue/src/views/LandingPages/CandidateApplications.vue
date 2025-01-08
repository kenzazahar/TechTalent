<template>
  <div class="layout">
    <Sidebar />
    <div class="main-content">
      <div class="applications-container">
        <h1 class="page-title">Mes Candidatures</h1>
        
        <!-- Statistiques -->
        <div class="status-summary">
          <div class="status-card">
            <div class="status-count">{{ applications.length }}</div>
            <div class="status-label">Total</div>
          </div>
          <div class="status-card">
            <div class="status-count pending">
              {{ applications.filter(app => app.status === 'En attente').length }}
            </div>
            <div class="status-label">En attente</div>
          </div>
          <div class="status-card">
            <div class="status-count accepted">
              {{ applications.filter(app => app.status === 'Acceptée').length }}
            </div>
            <div class="status-label">Acceptées</div>
          </div>
          <div class="status-card">
            <div class="status-count rejected">
              {{ applications.filter(app => app.status === 'Refusée').length }}
            </div>
            <div class="status-label">Refusées</div>
          </div>
        </div>

        <!-- Filtres -->
        <div class="filters">
          <input 
            type="text"
            v-model="searchText"
            placeholder="Rechercher une offre..."
            class="search-input"
          />
          <select v-model="statusFilter" class="status-filter">
            <option value="all">Tous les statuts</option>
            <option value="En attente">En attente</option>
            <option value="En cours">En cours</option>
            <option value="Acceptée">Acceptée</option>
            <option value="Refusée">Refusée</option>
          </select>
        </div>

        <!-- Liste des candidatures -->
        <div class="applications-list">
          <div v-for="(application, index) in filteredApplications" 
               :key="application.id" 
               class="application-item"
          >
            <div class="application-header">
              <h3>{{ application.jobTitle }}</h3>
              <span :class="['status-tag', application.status.toLowerCase()]">
                {{ application.status }}
              </span>
            </div>

            <div class="application-content">
              <div class="company-info">
                <img :src="application.companyLogo" :alt="application.company" class="company-logo">
                <div>
                  <div class="company-name">{{ application.company }}</div>
                  <div class="location">{{ application.location }}</div>
                </div>
              </div>

              <div class="application-details">
                <div class="detail-row">
                  <span>Postuler le: {{ formatDate(application.applicationDate) }}</span>
                </div>
                <div class="detail-row">
                  <span>Salaire: {{ application.salary }}</span>
                </div>
                <div class="detail-row">
                  <span>Type: {{ application.contractType }}</span>
                </div>
              </div>

              <div class="timeline">
                <div class="timeline-item" v-for="(event, eventIndex) in application.timeline" 
                     :key="eventIndex"
                >
                  <div class="timeline-dot"></div>
                  <div class="timeline-content">
                    <div class="event-date">{{ formatDate(event.date) }}</div>
                    <div class="event-description">{{ event.description }}</div>
                  </div>
                </div>
              </div>
            </div>

            <div class="application-actions">
              <button v-if="canWithdraw(application)" 
                      class="action-btn withdraw"
                      @click="confirmWithdraw(index)"
              >
                Retirer ma candidature
              </button>
            </div>
          </div>
        </div>

        <!-- Message si aucune candidature -->
        <div v-if="filteredApplications.length === 0" class="no-results">
          <p>Aucune candidature ne correspond à votre recherche</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import Sidebar from './components/SidebarCandidat.vue'

const searchText = ref('')
const statusFilter = ref('all')

const applications = ref([
{
      id: 1,
      jobTitle: 'Développeur Frontend Vue.js',
      company: 'TechCorp',
      companyLogo: '/src/assets/img/logo1.jpg',
      location: 'Casablanca',
      status: 'En attente',
      applicationDate: '2024-01-05',
      salary: '15000 - 20000 DH',
      contractType: 'CDI',
      timeline: [
        {
          date: '2024-01-05',
          description: 'Candidature soumise'
        },
        {
          date: '2024-01-07',
          description: 'CV consulté par le recruteur'
        }
      ]
    },
    {
      id: 2,
      jobTitle: 'UX/UI Designer',
      company: 'DesignStudio',
      companyLogo: '/src/assets/img/logo2.jpg',
      location: 'Rabat',
      status: 'En cours',
      applicationDate: '2024-01-03',
      salary: '12000 - 18000 DH',
      contractType: 'CDI',
      timeline: [
        {
          date: '2024-01-03',
          description: 'Candidature soumise'
        },
        {
          date: '2024-01-04',
          description: 'Entretien technique planifié'
        }
      ]
    }
])

const filteredApplications = computed(() => {
  return applications.value.filter(app => {
    const matchesSearch = app.jobTitle.toLowerCase().includes(searchText.value.toLowerCase()) ||
                         app.company.toLowerCase().includes(searchText.value.toLowerCase())
    const matchesStatus = statusFilter.value === 'all' || app.status === statusFilter.value
    return matchesSearch && matchesStatus
  })
})

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString('fr-FR', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

const canWithdraw = (application) => {
  return ['En attente', 'En cours'].includes(application.status)
}

const confirmWithdraw = (index) => {
  if (confirm('Êtes-vous sûr de vouloir retirer votre candidature ?')) {
    applications.value.splice(index, 1)
  }
}
</script>

<style scoped>
.layout {
  display: flex;
  background-color: #f9fafb;
  min-height: 100vh;
}

.main-content {
  flex: 1;
  margin-left: 260px;
  padding: 2rem;
}

.applications-container {
  max-width: 1200px;
  margin: 0 auto;
}

.page-title {
  font-size: 1.75rem;
  font-weight: 600;
  color: #111827;
  margin-bottom: 1.5rem;
}

.status-summary {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.status-card {
  background: white;
  padding: 1.25rem;
  border-radius: 0.5rem;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.status-count {
  font-size: 1.75rem;
  font-weight: 600;
}

.status-count.pending { color: #ea580c; }
.status-count.accepted { color: #059669; }
.status-count.rejected { color: #dc2626; }

.status-label {
  margin-top: 0.25rem;
  color: #6b7280;
  font-size: 0.875rem;
}

.filters {
  display: flex;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.search-input,
.status-filter {
  padding: 0.625rem 1rem;
  border: 1px solid #e5e7eb;
  border-radius: 0.375rem;
  background: white;
  font-size: 0.875rem;
}

.search-input {
  flex: 1;
}

.application-item {
  background: white;
  border-radius: 0.5rem;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
  margin-bottom: 1rem;
}

.application-header {
  padding: 1.25rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #e5e7eb;
}

.application-header h3 {
  margin: 0;
  font-size: 1.125rem;
  color: #111827;
}

.status-tag {
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 500;
}

.status-tag.en-attente { background: #fff7ed; color: #ea580c; }
.status-tag.en-cours { background: #eff6ff; color: #2563eb; }
.status-tag.acceptée { background: #ecfdf5; color: #059669; }
.status-tag.refusée { background: #fef2f2; color: #dc2626; }

.application-content {
  padding: 1.25rem;
}

.company-info {
  display: flex;
  gap: 1rem;
  margin-bottom: 1.25rem;
}

.company-logo {
  width: 48px;
  height: 48px;
  border-radius: 0.375rem;
  object-fit: cover;
}

.company-name {
  font-weight: 500;
  color: #374151;
}

.location {
  color: #6b7280;
  font-size: 0.875rem;
  margin-top: 0.25rem;
}

.application-details {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 1rem;
  margin-bottom: 1.25rem;
}

.detail-row {
  color: #6b7280;
  font-size: 0.875rem;
}

.timeline {
  border-left: 2px solid #e5e7eb;
  margin-left: 0.75rem;
  padding-left: 1.5rem;
}

.timeline-item {
  position: relative;
  margin-bottom: 1.25rem;
}

.timeline-dot {
  position: absolute;
  left: -1.75rem;
  width: 0.625rem;
  height: 0.625rem;
  border-radius: 9999px;
  background: #34343d;
}

.event-date {
  font-size: 0.75rem;
  color: #6b7280;
}

.event-description {
  color: #374151;
  margin-top: 0.25rem;
  font-size: 0.875rem;
}

.application-actions {
  padding: 1.25rem;
  border-top: 1px solid #e5e7eb;
}

.action-btn.withdraw {
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  font-size: 0.875rem;
  font-weight: 500;
  background: white;
  color: #dc2626;
  border: 1px solid #dc2626;
  cursor: pointer;
  transition: all 0.2s;
}

.action-btn.withdraw:hover {
  background: #fef2f2;
}

.no-results {
  text-align: center;
  padding: 2rem;
  color: #6b7280;
}
</style>