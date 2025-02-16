<template>
  <div class="flex">
    <Sidebar />
    <div class="main-content">
      <div class="container">
        <h2 class="title">Liste des candidatures</h2>

        <div class="filters">
          <input v-model="searchQuery" placeholder="Rechercher..." class="search" />
          <select v-model="statusFilter" class="filter">
            <option value="all">Tous les statuts</option>
            <option v-for="(label, status) in statusLabels" :key="status" :value="status">
              {{ label }}
            </option>
          </select>
        </div>

        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th>Nom complet</th>
                <th>Email</th>
                <th>Téléphone</th>
                <th>Date de candidature</th>
                <th>Documents</th>
                <th>Status</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="candidate in filteredCandidates" :key="candidate.id">
                <td>{{ candidate.student_nom }} {{ candidate.student_prenom }}</td>
                <td>{{ candidate.student_email }}</td>
                <td>{{ candidate.student_telephone }}</td>
                <td>{{ formatDate(candidate.application_date) }}</td>
                <td>
                  <div class="flex gap-2">
                    <a v-if="candidate.cv" :href="candidate.cv" class="doc-link">
                      <i class="fas fa-file-pdf"></i> CV
                    </a>
                    <a v-if="candidate.cover_letter" :href="candidate.cover_letter" class="doc-link">
                      <i class="fas fa-file-alt"></i> LM
                    </a>
                  </div>
                </td>
                <td>
                  <span :class="['status', candidate.status]">
                    {{ statusLabels[candidate.status] }}
                  </span>
                </td>
                <td>
                  <div class="actions">
                    <select v-model="candidate.status" @change="updateStatus(candidate.id, $event)" class="action-select">
                      <option v-for="(label, status) in statusLabels" :key="status" :value="status">
                        {{ label }}
                      </option>
                    </select>
                    <button @click="contactCandidate(candidate)" class="btn-contact">
                      <i class="fas fa-paper-plane"></i>
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import Sidebar from './components/Sidebar.vue';
import { useRoute } from 'vue-router';
import { getCompanyApplications, updateApplicationStatus } from '@/apiClient';

const route = useRoute();
const offerId = route.params.id;  // Récupère l'ID de l'offre depuis l'URL

const searchQuery = ref('');
const statusFilter = ref('all');
const applications = ref([]);

const statusLabels = {
  pending: 'En attente',
  reviewing: "En cours d'examen",
  interviewed: 'Entretien effectué',
  accepted: 'Acceptée',
  rejected: 'Refusée'
};

onMounted(async () => {
  try {
    const response = await getCompanyApplications(offerId);
    applications.value = response.applications;
  } catch (error) {
    console.error('Erreur lors de la récupération des candidatures:', error);
  }
});

const filteredCandidates = computed(() => {
  return applications.value.filter(candidate => {
    const matchesSearch = 
      `${candidate.student_nom} ${candidate.student_prenom}`.toLowerCase()
      .includes(searchQuery.value.toLowerCase());
    const matchesStatus = statusFilter.value === 'all' || candidate.status === statusFilter.value;
    return matchesSearch && matchesStatus;
  });
});

const formatDate = (date) => new Date(date).toLocaleDateString('fr-FR');

const updateStatus = async (candidateId, event) => {
  try {
    const newStatus = event.target.value;
    await updateApplicationStatus(candidateId, newStatus);
    const candidate = applications.value.find(app => app.id === candidateId);
    if (candidate) {
      candidate.status = newStatus;
    }
  } catch (error) {
    console.error('Erreur lors de la mise à jour du statut:', error);
  }
};

const contactCandidate = (candidate) => {
  console.log(`Contacter ${candidate.student_nom} ${candidate.student_prenom}`);
};
</script>

  
<style scoped>
  .main-content {
    margin-left: 260px;
    min-height: 100vh;
    background: #f9fafb;
    padding: 2rem;
  }
  
  .container {
    max-width: 1400px;
    margin: 0 auto;
  }
  
  .title {
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 1.5rem;
    color: #111827;
  }
  
  .filters {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.5rem;
  }
  
  .search, .filter {
    padding: 0.5rem 1rem;
    border: 1px solid #e5e7eb;
    border-radius: 0.375rem;
  }
  
  .search {
    flex: 1;
  }
  
  .table-container {
    background: white;
    border-radius: 0.5rem;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    overflow-x: auto;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
  }
  
  th {
    background: #f9fafb;
    padding: 0.75rem 1rem;
    text-align: left;
    font-weight: 600;
    color: #4b5563;
    border-bottom: 1px solid #e5e7eb;
  }
  
  td {
    padding: 0.75rem 1rem;
    border-bottom: 1px solid #e5e7eb;
    color: #111827;
  }
  
  .status {
    padding: 0.25rem 0.75rem;
    border-radius: 9999px;
    font-size: 0.875rem;
    font-weight: 500;
  }
  
  .status.pending { background: #fff7ed; color: #ea580c; }
  .status.reviewing { background: #eff6ff; color: #2563eb; }
  .status.interviewed { background: #f0fdf4; color: #16a34a; }
  .status.accepted { background: #ecfdf5; color: #059669; }
  .status.rejected { background: #fef2f2; color: #dc2626; }
  
  .actions {
    display: flex;
    gap: 0.5rem;
    align-items: center;
  }
  
  .action-select {
    padding: 0.25rem 0.5rem;
    border: 1px solid #e5e7eb;
    border-radius: 0.375rem;
    font-size: 0.875rem;
  }
  
  .btn-contact {
    padding: 0.25rem 0.5rem;
    background: #1f2937;
    color: white;
    border-radius: 0.375rem;
    font-size: 0.875rem;
  }
  
  .doc-link {
    color: #4b5563;
    text-decoration: none;
    font-size: 0.875rem;
  }
  
  .doc-link:hover {
    color: #111827;
  }
</style>