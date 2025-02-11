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
                  <td>{{ candidate.firstName }} {{ candidate.lastName }}</td>
                  <td>{{ candidate.email }}</td>
                  <td>{{ candidate.phone }}</td>
                  <td>{{ formatDate(candidate.applicationDate) }}</td>
                  <td>
                    <div class="flex gap-2">
                        <router-link 
        v-if="candidate.cv" 
        :to="{ name: 'CandidateCV', params: { id: candidate.id }}"
        class="doc-link"
      >
        <i class="fas fa-file-pdf"></i> CV
      </router-link>
      <a v-if="candidate.coverLetter" :href="candidate.coverLetter" class="doc-link">
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
  import { ref, computed } from 'vue'
  import Sidebar from './components/Sidebar.vue'
  
  const searchQuery = ref('')
  const statusFilter = ref('all')
  
  const statusLabels = {
    pending: 'En attente',
    reviewing: "En cours d'examen",
    interviewed: 'Entretien effectué',
    accepted: 'Acceptée',
    rejected: 'Refusée'
  }
  
  const candidates = ref([
  {
    id: 1,
    firstName: 'Youssef',
    lastName: 'El Amrani',
    email: 'youssef.elamrani@gmail.com',
    phone: '+212 661-234567',
    cv: '/docs/cv_elamrani.pdf',
    coverLetter: '/docs/lm_elamrani.pdf',
    status: 'pending',
    applicationDate: '2024-01-05'
  },
  {
    id: 2,
    firstName: 'Fatima',
    lastName: 'Benkirane',
    email: 'f.benkirane@outlook.com',
    phone: '+212 662-345678',
    cv: '/docs/cv_benkirane.pdf',
    coverLetter: '/docs/lm_benkirane.pdf',
    status: 'reviewing',
    applicationDate: '2024-01-08'
  },
  {
    id: 3,
    firstName: 'Karim',
    lastName: 'Ouazzani',
    email: 'k.ouazzani@yahoo.com',
    phone: '+212 663-456789',
    cv: '/docs/cv_ouazzani.pdf',
    coverLetter: '/docs/lm_ouazzani.pdf',
    status: 'interviewed',
    applicationDate: '2024-01-10'
  },
  {
    id: 4,
    firstName: 'Nadia',
    lastName: 'Tazi',
    email: 'nadia.tazi@gmail.com',
    phone: '+212 664-567890',
    cv: '/docs/cv_tazi.pdf',
    coverLetter: '/docs/lm_tazi.pdf',
    status: 'accepted',
    applicationDate: '2024-01-12'
  },
  {
    id: 5,
    firstName: 'Hassan',
    lastName: 'El Fassi',
    email: 'h.elfassi@gmail.com',
    phone: '+212 665-678901',
    cv: '/docs/cv_elfassi.pdf',
    coverLetter: '/docs/lm_elfassi.pdf',
    status: 'rejected',
    applicationDate: '2024-01-15'
  }
  ])
  
  const filteredCandidates = computed(() => {
    return candidates.value.filter(candidate => {
      const matchesSearch = 
        `${candidate.firstName} ${candidate.lastName}`.toLowerCase()
        .includes(searchQuery.value.toLowerCase())
      const matchesStatus = statusFilter.value === 'all' || candidate.status === statusFilter.value
      return matchesSearch && matchesStatus
    })
  })
  
  const formatDate = (date) => new Date(date).toLocaleDateString('fr-FR')
  
  const updateStatus = (candidateId, event) => {
    console.log(`Statut mis à jour pour ${candidateId}: ${event.target.value}`)
  }
  
  const contactCandidate = (candidate) => {
    console.log(`Contacter ${candidate.firstName} ${candidate.lastName}`)
  }
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