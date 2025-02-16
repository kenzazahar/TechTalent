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
              {{ getPendingCount }}
            </div>
            <div class="status-label">En attente</div>
          </div>
          <div class="status-card">
            <div class="status-count accepted">
              {{ getAcceptedCount }}
            </div>
            <div class="status-label">Acceptées</div>
          </div>
          <div class="status-card">
            <div class="status-count rejected">
              {{ getRejectedCount }}
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
            <option value="pending">En attente</option>
            <option value="reviewing">En cours d'examen</option>
            <option value="interviewed">Entretien effectué</option>
            <option value="accepted">Acceptée</option>
            <option value="rejected">Refusée</option>
          </select>
        </div>

        <!-- Liste des candidatures -->
        <div v-if="applications.length > 0" class="applications-list">
          <div v-for="application in filteredApplications" 
               :key="application.id" 
               class="application-item"
          >
            <div class="application-header">
              <h3>{{ application.job_title }}</h3>
              <span :class="['status-tag', application.status]">
                {{ getStatusLabel(application.status) }}
              </span>
            </div>

            <div class="application-content">
              <div class="company-info">
                <img :src="application.company_logo || '/default-company-logo.png'" 
                     :alt="application.company_name" 
                     class="company-logo">
                <div>
                  <div class="company-name">{{ application.company_name }}</div>
                  <div class="location">{{ application.location }}</div>
                </div>
              </div>

              <div class="application-details">
                <div class="detail-row">
                  <span>Postuler le: {{ formatDate(application.application_date) }}</span>
                </div>
                <div class="detail-row">
                  <span>Salaire: {{ application.salary || 'Non spécifié' }}</span>
                </div>
                <div class="detail-row">
                  <span>Type de contrat: {{ application.contract_type }}</span>
                </div>
              </div>
            </div>

            <div class="application-actions">
              <button v-if="canWithdraw(application)" 
                      class="action-btn withdraw"
                      @click="confirmWithdraw(application.id)"
              >
                Retirer ma candidature
              </button>
            </div>
          </div>
        </div>

        <!-- Message si aucune candidature -->
        <div v-else class="no-results">
          <p>Vous n'avez pas encore soumis de candidature</p>
        </div>

        <div v-if="applications.length > 0 && filteredApplications.length === 0" class="no-results">
          <p>Aucune candidature ne correspond à votre recherche</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import Sidebar from './components/SidebarCandidat.vue'
import { getStudentApplications, deleteApplication } from '@/apiClient'

const searchText = ref('')
const statusFilter = ref('all')
const applications = ref([])
const loading = ref(false)
const error = ref(null)

// Computed properties for statistics
const getPendingCount = computed(() => 
  applications.value.filter(app => app.status === 'pending').length
)

const getAcceptedCount = computed(() => 
  applications.value.filter(app => app.status === 'accepted').length
)

const getRejectedCount = computed(() => 
  applications.value.filter(app => app.status === 'rejected').length
)

const filteredApplications = computed(() => {
  return applications.value.filter(app => {
    const matchesSearch = 
      app.job_title?.toLowerCase().includes(searchText.value.toLowerCase()) ||
      app.company_name?.toLowerCase().includes(searchText.value.toLowerCase());
    
    const matchesStatus = statusFilter.value === 'all' || app.status === statusFilter.value;
    
    return matchesSearch && matchesStatus;
  });
})

const getStatusLabel = (status) => {
  const statusMap = {
    'pending': 'En attente',
    'reviewing': "En cours d'examen",
    'interviewed': 'Entretien effectué',
    'accepted': 'Acceptée',
    'rejected': 'Refusée'
  }
  return statusMap[status] || status
}

const formatDate = (dateString) => {
  if (!dateString) return ''
  return new Date(dateString).toLocaleDateString('fr-FR', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

const canWithdraw = (application) => {
  return ['pending', 'reviewing'].includes(application.status)
}

const loadApplications = async () => {
  loading.value = true
  error.value = null
  try {
    const response = await getStudentApplications()
    applications.value = response.applications
    console.log('Applications loaded:', applications.value)
  } catch (err) {
    error.value = 'Erreur lors du chargement des candidatures'
    console.error('Error loading applications:', err)
  } finally {
    loading.value = false
  }
}

const confirmWithdraw = async (applicationId) => {
  if (confirm('Êtes-vous sûr de vouloir retirer votre candidature ?')) {
    try {
      await deleteApplication(applicationId)
      applications.value = applications.value.filter(app => app.id !== applicationId)
    } catch (error) {
      console.error('Erreur lors du retrait de la candidature:', error)
      alert('Erreur lors du retrait de la candidature')
    }
  }
}

onMounted(() => {
  loadApplications()
})
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