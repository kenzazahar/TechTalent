<template>
    <div class="layout">
      <Sidebar />
      <div class="main-content">
        <div class="job-offers-dashboard">
          <!-- Section recherche avancée -->
          <div class="header-box">
            <h2 class="section-title">Recherche avancée</h2>
            
            <!-- Barre de recherche principale -->
            <div class="search-container">
              <input 
                type="text" 
                v-model="store.filters.search"
                placeholder="Rechercher une offre..." 
                class="search-input"
              />
              <i class="fas fa-search search-icon"></i>
            </div>
  
            <!-- Filtres -->
            <div class="filters-grid">
              <!-- Type de contrat -->
              <div class="filter-group">
                <label class="filter-label">Type de contrat</label>
                <select
                  v-model="store.filters.contractType"
                  class="filter-select"
                >
                  <option value="">Tous</option>
                  <option value="CDI">CDI</option>
                  <option value="CDD">CDD</option>
                  <option value="Stage">Stage</option>
                </select>
              </div>
  
              <!-- Localisation -->
              <div class="filter-group">
                <label class="filter-label">Localisation</label>
                <input
                  type="text"
                  v-model="store.filters.location"
                  placeholder="Entrez une ville"
                  class="filter-input"
                />
              </div>
  
              <!-- Mode de travail -->
              <div class="filter-group">
                <label class="filter-label">Mode de travail</label>
                <select
                  v-model="store.filters.workMode"
                  class="filter-select"
                >
                  <option value="">Tous</option>
                  <option value="Hybride">Hybride</option>
                  <option value="Télétravail">Télétravail</option>
                  <option value="Sur site">Sur site</option>
                </select>
              </div>
            </div>
  
            <!-- Range pour le salaire -->
            <div class="salary-filter">
              <label class="filter-label">
                Salaire (kDh): {{ store.filters.minSalary }}k - {{ store.filters.maxSalary }}k
              </label>
              <div class="salary-range">
                <input
                  type="range"
                  v-model.number="store.filters.minSalary"
                  min="0"
                  max="150"
                  class="range-input"
                />
                <input
                  type="range"
                  v-model.number="store.filters.maxSalary"
                  min="0"
                  max="150"
                  class="range-input"
                />
              </div>
            </div>
  
            <!-- Bouton réinitialiser -->
            <button
              @click="store.resetFilters"
              class="reset-btn"
            >
              Réinitialiser les filtres
            </button>
          </div>
  
          <!-- Liste des offres -->
          <section class="offers-section">
            <h2 class="section-title">Offres disponibles</h2>
            <div class="offers-grid">
              <div
                v-for="offer in store.filteredOffers"
                :key="offer.id"
                class="offer-card"
                :style="{ backgroundImage: `url(${offer.image})` }"
              >
                <div class="card-content">
                  <h3 class="offer-title">{{ offer.title }}</h3>
                  <p class="offer-location">{{ offer.contractType }} - {{ offer.location }}</p>
                  <div class="offer-tags">
                    <span 
                      v-for="tag in offer.tags" 
                      :key="tag"
                      class="tag"
                    >
                      {{ tag }}
                    </span>
                  </div>
                  <button
                    @click="$router.push(`/candidate/dashboard/offers/${offer.id}`)"
                    class="action-btn btn-explore"
                  >
                    Voir le détail
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
  import Sidebar from './components/SidebarCandidat.vue';
  import { useCandidateJobStore } from '@/stores/candidateJobStore';
  import { useRouter } from 'vue-router';
  
  const store = useCandidateJobStore();
  const router = useRouter();
</script>
  
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
  }
  
  .header-box {
    background: rgb(253, 250, 250);
    border-radius: 0.5rem;
    box-shadow: 0 1px 3px rgba(4, 2, 10, 0.1);
    padding: 1.5rem;
    margin-bottom: 2rem;
  }
  
  .section-title {
    font-size: 1.25rem;
    font-weight: 600;
    color: #464242;
    margin-bottom: 1.5rem;
  }
  
  .search-container {
    position: relative;
    margin-bottom: 1.5rem;
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
    color: #9CA3AF;
  }
  
  .filters-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
    margin-bottom: 1.5rem;
  }
  
  .filter-group {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .filter-label {
    font-size: 0.875rem;
    font-weight: 500;
    color: #4B5563;
  }
  
  .filter-select,
  .filter-input {
    padding: 0.5rem;
    border: 1px solid #e5e7eb;
    border-radius: 0.375rem;
    outline: none;
    background: white;
  }
  
  .salary-filter {
    margin-bottom: 1.5rem;
  }
  
  .salary-range {
    display: flex;
    gap: 1rem;
  }
  
  .range-input {
    flex: 1;
  }
  
  
  .reset-btn {
    background-color: #34343d;
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 0.375rem;
    transition: background-color 0.2s;
  }
  
  .reset-btn:hover {
    background-color: #1e1d1e;
  }
  
  .offers-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
  }
  
  .offer-card {
    position: relative;
    border-radius: 0.5rem;
    overflow: hidden;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    background-size: cover;
    background-position: center;
    min-height: 300px;
    transition: transform 0.2s;
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
    background: rgba(255, 255, 255, 0.9);
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
  
  .offer-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1rem;
  }
  
  .tag {
    padding: 0.25rem 0.75rem;
    background: rgba(0, 0, 0, 0.05);
    border-radius: 1rem;
    font-size: 0.75rem;
    color: #4B5563;
  }
  
  .action-btn {
    width: 100%;
    padding: 0.75rem;
    border-radius: 0.375rem;
    transition: all 0.2s;
    text-align: center;
  }
  
  .btn-explore {
    background-color: #1e2023;
    color: white;
  }
  
  .btn-explore:hover {
    background-color: #0c0c0c;
  }
</style>