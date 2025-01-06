<template>
  <div class="layout">
    <Sidebar />
    <div class="main-content">
  <div class="job-offers-dashboard bg-gray-100">
    <!-- Header box avec recherche et bouton -->
    <div class="header-box">
      <div class="search-container">
        <input 
          type="text" 
          v-model="searchQuery" 
          placeholder="Rechercher une offre..." 
          class="search-input"
          @keyup.enter="handleSearch"
        />
        <i class="fas fa-search search-icon cursor-pointer" @click="handleSearch"></i>
      </div>
      <button @click="$router.push('/dashboard/new-offer')" class="new-offer-btn">
        Nouvelle offre
      </button>
    </div>

    <!-- Section des offres publiées -->
    <section class="offers-section">
      <h2 class="section-title">Offres publiées</h2>
      <div class="offers-grid">
        <div 
          v-for="offer in filteredPublishedOffers" 
          :key="offer.id" 
          class="offer-card"
          :style="{ backgroundImage: `url(${offer.image})` }"
        >
          <div class="card-content">
            <h3 class="offer-title">{{ offer.title }}</h3>
            <p class="offer-location">{{ offer.location }}</p>
            <div class="offer-actions">
              <button class="action-btn btn-explore" @click="$router.push(`/dashboard/offers/${offer.id}`)">
                Explorer
              </button>
              <button class="action-btn btn-manage">
                Gestion candidatures
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section des brouillons -->
    <section class="drafts-section">
      <h2 class="section-title">Brouillons</h2>
      <div class="offers-grid">
        <div 
          v-for="draft in filteredDraftOffers" 
          :key="draft.id" 
          class="offer-card draft"
          :style="{ backgroundImage: `url(${draft.image})` }"
        >
          <div class="card-content">
            <h3 class="offer-title">{{ draft.title }}</h3>
            <p class="offer-location">{{ draft.location }}</p>
            <button class="action-btn btn-edit" @click="$router.push(`/dashboard/drafts/${draft.id}/edit`)">
              Continuer l'édition
            </button>
          </div>
        </div>
      </div>
     </section>
    </div>
   </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useJobOffersStore } from 'C:/Vue_Django/App-vue/src/stores/jobOffersStore.js';
import Sidebar from './components/Sidebar.vue';

const searchQuery = ref('');
const jobOffersStore = useJobOffersStore();



// Fonction de filtrage des offres
const filterOffers = (offers) => {
  const query = searchQuery.value.toLowerCase().trim();
  if (!query) return offers;
  return offers.filter(offer => 
    offer.title.toLowerCase().includes(query) || 
    offer.location.toLowerCase().includes(query)
  );
};

// Computed properties pour les offres filtrées
const filteredPublishedOffers = computed(() => 
  filterOffers(jobOffersStore.publishedOffers)
);
const filteredDraftOffers = computed(() => 
  filterOffers(jobOffersStore.draftOffers)
);

// Fonction de recherche
const handleSearch = () => {
  // La recherche est automatique grâce aux computed properties
  // Mais on pourrait ajouter ici d'autres actions comme le tracking
  console.log('Recherche effectuée:', searchQuery.value);
};
</script>

<!-- Le style reste exactement le même que dans votre code -->
<style scoped>
.layout {
  display: flex;
  width: 100%;
  min-height: 100vh;
}

.main-content {
  flex: 1;
  margin-left: 260px; /* Largeur de la sidebar */
  padding: 20px;
}
.job-offers-dashboard {
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  min-height: 100vh;
}

.header-box {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  background: rgb(253, 250, 250);
  border-radius: 0.5rem;
  box-shadow: 0 1px 3px rgba(4, 2, 10, 0.1);
  margin-bottom: 2rem;
  position: relative;
}

.search-container {
  position: relative;
  flex-grow: 1;
  margin-right: 1rem;
}

.search-input {
  width: 100%;
  padding: 0.5rem 1rem 0.5rem 2.5rem;
  border: 1px solid #e5e7eb;
  border-radius: 0.375rem;
  outline: none;
}

.search-input:focus {
  border-color: #0d0331;
  box-shadow: 0 0 0 2px rgba(150, 90, 5, 0.2);
}

.search-icon {
  position: absolute;
  left: 0.75rem;
  top: 50%;
  transform: translateY(-50%);
  color: #9CA3AF;
}

.new-offer-btn {
  background-color: #34343d;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  transition: background-color 0.2s;
  position: absolute;
  right: 1.5rem;
}

.new-offer-btn:hover {
  background-color: #1e1d1e;
}

.section-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: #464242;
  margin-bottom: 1rem;
}

.offers-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.offer-card {
  position: relative;
  border-radius: 0.5rem;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s;
  background-size: cover;
  background-position: center;
  min-height: 300px;
}

.offer-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.card-content {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 1.5rem;
  background: rgba(255, 255, 255, 0.3);
  backdrop-filter: blur(5px);
}

.offer-title {
  font-size: 1.125rem;
  font-weight: 600;
  color: #202124;
  margin-bottom: 0.5rem;
}

.offer-location {
  font-size: 0.875rem;
  color: #0a0a0a;
  margin-bottom: 1rem;
}

.offer-actions {
  display: flex;
  justify-content: space-between;
  gap: 0.5rem;
}

.action-btn {
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  transition: all 0.2s;
}

.btn-explore {
  background-color: #1e2023;
  color: white;
}

.btn-explore:hover {
  background-color: #0c0c0c;
}

.btn-manage {
  background-color: #34343d;
  color: #fdfeff;
}

.btn-manage:hover {
  background-color: #101011;
}

.btn-edit {
  background-color: #27272c;
  color: #eaedf2;
  width: 100%;
}

.btn-edit:hover {
  background-color: #030303;
}

.draft {
  opacity: 0.85;
}
.search-icon {
  cursor: pointer;
}

.search-icon:hover {
  color: #0d0331;
}
</style>