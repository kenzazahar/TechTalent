<script setup>
import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useJobOffersStore } from '@/stores/jobOffersStore.js';

const router = useRouter();
const route = useRoute();
const jobOffersStore = useJobOffersStore();
const showDeleteModal = ref(false);

const offer = ref(null);

onMounted(() => {
  const offerId = parseInt(route.params.id);
  offer.value = jobOffersStore.publishedOffers.find(o => o.id === offerId);
  
  if (!offer.value) {
    router.push('/dashboard');
  }
});

const handleEdit = () => {
  router.push({ 
    name: 'EditOffer', 
    params: { id: offer.value.id }
  });
};

const handleDelete = () => {
  showDeleteModal.value = true;
};

const confirmDelete = async () => {
  try {
    await jobOffersStore.deletePublishedOffer(offer.value.id);
    showDeleteModal.value = false;
    router.push('/dashboard');
  } catch (error) {
    console.error('Erreur lors de la suppression:', error);
  }
};

const handleClose = () => {
  router.push('/dashboard');
};
</script>

<template>
  <div class="page-wrapper">
    <div class="offer-detail-page" v-if="offer">
      <div class="offer-container">
        <div class="image-container" :style="{ backgroundImage: `url(${offer.image || '/default-offer.jpg'})` }">
          <div class="content-overlay">
            <div class="header">
              <h2>{{ offer.title }}</h2>
              <p class="location">{{ offer.location }}</p>
            </div>

            <div class="content">
              <div class="info-section">
                <h3>Description</h3>
                <p>{{ offer.shortDescription }}</p>
              </div>

              <div class="info-grid">
                <div class="info-item">
                  <h4>Type de contrat</h4>
                  <p>{{ offer.contractType }}</p>
                </div>
                <div class="info-item">
                  <h4>Mode de travail</h4>
                  <p>{{ offer.workMode }}</p>
                </div>
                <div class="info-item">
                  <h4>Durée</h4>
                  <p>{{ offer.offerDuration || 'Non spécifié' }}</p>
                </div>
                <div class="info-item">
                  <h4>Salaire</h4>
                  <p>{{ offer.salary || 'Non spécifié' }}</p>
                </div>
              </div>

              <div class="recruiter-section">
                <h3>Recruteur</h3>
                <p><strong>{{ offer.recruiterName }}</strong></p>
                <p>{{ offer.recruiterEmail }}</p>
                <p>{{ offer.recruiterPhone || 'Non spécifié' }}</p>
              </div>
            </div>

            <div class="actions">
              <button @click="handleEdit" class="btn-edit">Modifier</button>
              <button @click="handleDelete" class="btn-delete">Supprimer</button>
              <button @click="handleClose" class="btn-close">Fermer</button>
            </div>
          </div>
        </div>
      </div>

      <!-- Modal de confirmation -->
      <div class="modal" v-if="showDeleteModal">
        <div class="modal-content">
          <h3>Confirmation</h3>
          <p>Supprimer cette offre ?</p>
          <div class="modal-actions">
            <button @click="confirmDelete" class="btn-confirm">Oui</button>
            <button @click="showDeleteModal = false" class="btn-cancel">Non</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.page-wrapper {
  min-height: 100vh;
  background-color: #202020;
  padding: 2rem;
  box-sizing: border-box;
}

.offer-detail-page {
  max-width: 900px;
  margin: 0 auto;
  background: transparent;
}

.offer-container {
  width: 100%;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.image-container {
  width: 100%;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  height: 100%;
  position: relative;
}

.content-overlay {
  background: rgba(0, 0, 0, 0.75);
  padding: 2rem;
  color: white;
  min-height: 100%;
}

.header {
  text-align: center;
  margin-bottom: 2rem;
}

.header h2 {
  font-size: 2rem;
  margin: 0 0 0.5rem 0;
  color: #fff;
}

.location {
  font-size: 1.1rem;
  color: #ddd;
  margin: 0;
}

.content {
  margin-bottom: 2rem;
}

.info-section {
  margin-bottom: 2rem;
}

.info-section h3 {
  font-size: 1.3rem;
  margin-bottom: 1rem;
  color: #fff;
  border-bottom: 2px solid #555158;
  padding-bottom: 0.5rem;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
  margin: 2rem 0;
}

.info-item {
  background: rgba(255, 255, 255, 0.1);
  padding: 1rem;
  border-radius: 8px;
  backdrop-filter: blur(5px);
}

.info-item h4 {
  margin: 0 0 0.5rem 0;
  font-size: 1rem;
  color: #01060b;
}

.info-item p {
  margin: 0;
  font-size: 1.1rem;
}

.recruiter-section {
  background: rgba(255, 255, 255, 0.1);
  padding: 1.5rem;
  border-radius: 8px;
  margin-top: 2rem;
}

.recruiter-section h3 {
  color: #01060b;
  margin: 0 0 1rem 0;
}

.recruiter-section p {
  margin: 0.5rem 0;
}

.actions {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-top: 2rem;
}

/* Style commun pour tous les boutons */
.btn-edit, .btn-delete, .btn-close {
  width: 180px;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-weight: 600;
  width: 150px;
  text-align: center;
  color: white;
}

.actions button {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-weight: 600;
  flex: 1; /* Permet aux boutons de prendre la même largeur */
  max-width: 180px; /* Ajuste selon la largeur souhaitée */
}

.actions button:hover {
  transform: translateY(-2px);
  opacity: 0.9;
}

.btn-edit {
  background: #544f55;
  display: inline-block;
  width: 150px; /* Ajuste selon tes besoins */
  height: 45px;
}

.btn-delete {
  background: #2e2a2f;
  display: inline-block;
  width: 150px; /* Ajuste selon tes besoins */
  height: 45px;
}

.btn-close {
  background: #2e2a2f;
  display: inline-block;
  width: 90px; /* Ajuste selon tes besoins */
  height: 23px;
}

@media (max-width: 768px) {
  .btn-edit, .btn-delete, .btn-close {
    width: 100%;
  }
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  background: rgba(0, 0, 0, 0.5);
  z-index: 1000;
}

.modal-content {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  width: 90%;
  max-width: 400px;
  text-align: center;
  color: #333;
}

.modal-actions {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-top: 1.5rem;
}

.modal-actions button {
  padding: 0.5rem 1.5rem;
  border: none;
  border-radius: 5px;
  font-weight: 600;
  cursor: pointer;
}

.btn-confirm {
  background: #dc3545;
  color: white;
}

.btn-cancel {
  background: #6c757d;
  color: white;
}

@media (max-width: 768px) {
  .page-wrapper {
    padding: 1rem;
  }

  .info-grid {
    grid-template-columns: 1fr;
  }

  .actions {
    flex-direction: column;
  }

  .actions button {
    width: 100%;
  }
}
</style>