<template>
    <div class="offer-detail-page">
      <template v-if="offer">
        <div v-if="!showApplicationForm" class="main-content">
          <!-- En-tête de l'offre -->
          <div class="offer-header">
            <img :src="offer.image" :alt="offer.title" class="offer-image" />
            <div class="offer-header-content">
              <h1 class="title">{{ offer.title }}</h1>
              <div class="offer-info">
                <span class="info-item">
                  <i class="fas fa-map-marker-alt"></i>
                  {{ offer.location }}
                </span>
                <span class="info-item">
                  <i class="fas fa-briefcase"></i>
                  {{ offer.contractType }}
                </span>
                <span class="info-item">
                  <i class="fas fa-building"></i>
                  {{ offer.workMode }}
                </span>
                <span class="info-item">
                  <i class="fas fa-money-bill-wave"></i>
                  {{ offer.salary }}k DH
                </span>
              </div>
            </div>
          </div>
  
          <!-- Contenu principal -->
          <div class="offer-content">
            <div class="content-section">
              <h2 class="section-title">Description du poste</h2>
              <p class="description">{{ offer.description }}</p>
            </div>
  
            <div class="content-section">
              <h2 class="section-title">Compétences requises</h2>
              <div class="tags-container">
                <span 
                  v-for="tag in offer.tags" 
                  :key="tag"
                  class="tag"
                >
                  {{ tag }}
                </span>
              </div>
            </div>
  
            <div class="content-section">
              <h2 class="section-title">À propos de nous</h2>
              <p class="about-text">
                Nous sommes une entreprise leader dans notre domaine, cherchant à renforcer 
                nos équipes avec des talents passionnés et motivés.
              </p>
            </div>
  
            <!-- Boutons d'action -->
            <div class="action-buttons">
              <button @click="handleApply" class="btn-apply">
                Postuler
              </button>
              <button @click="handleCancel" class="btn-cancel">
                Annuler
              </button>
            </div>
          </div>
        </div>
        <ApplicationForm
          v-else
          :offer="offer"
          @cancel="showApplicationForm = false"
        />
      </template>
      <div v-else class="error-state">
        <h2>Chargement de l'offre...</h2>
      </div>
    </div>
  </template>
  
<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useCandidateJobStore } from '@/stores/candidateJobStore';
import ApplicationForm from './ApplicationForm.vue';
const showApplicationForm = ref(false);


const route = useRoute();
const router = useRouter();
const store = useCandidateJobStore();

const offer = ref(null);

onMounted(async () => {
  try {
    const offerId = parseInt(route.params.id);
    // Recherche de l'offre dans le store
    const foundOffer = store.jobOffers.find(o => o.id === offerId);
    
    if (foundOffer) {
      offer.value = foundOffer;
    } else {
      console.error('Offre non trouvée:', offerId);
      router.push('/dashboard'); // Redirection vers le dashboard si l'offre n'existe pas
    }
  } catch (error) {
    console.error('Erreur lors du chargement de l\'offre:', error);
    router.push('/dashboard');
  }
});

const handleApply = () => {
  showApplicationForm.value = true;
};

const handleCancel = () => {
  router.push('/candidate/dashboard');
};
</script>

<style scoped>
.error-state {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 400px;
  text-align: center;
  color: #666;
}

/* Le reste des styles reste inchangé */
.offer-detail-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.offer-header {
  background: white;
  border-radius: 0.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  margin-bottom: 2rem;
}

.offer-image {
  width: 100%;
  height: 300px;
  object-fit: cover;
}

.offer-header-content {
  padding: 2rem;
}

.title {
  font-size: 2rem;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 1rem;
}

.offer-info {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.info-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #4B5563;
}

.offer-content {
  background: white;
  border-radius: 0.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  padding: 2rem;
}

.content-section {
  margin-bottom: 2rem;
}

.section-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1a1a1a;
  margin-bottom: 1rem;
}

.description {
  color: #4B5563;
  line-height: 1.6;
}

.tags-container {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.tag {
  padding: 0.5rem 1rem;
  background: #F3F4F6;
  border-radius: 2rem;
  color: #4B5563;
  font-size: 0.875rem;
}

.action-buttons {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
  padding-top: 2rem;
  border-top: 1px solid #E5E7EB;
}

.btn-apply, .btn-cancel {
  padding: 0.75rem 2rem;
  border-radius: 0.375rem;
  font-weight: 500;
  transition: all 0.2s;
}

.btn-apply {
  background-color: #1d1d21;
  color: white;
  flex: 1;
}

.btn-apply:hover {
  background-color: #070507;
}

.btn-cancel {
  background-color: #F3F4F6;
  color: #4B5563;
}

.btn-cancel:hover {
  background-color: #E5E7EB;
}
</style>