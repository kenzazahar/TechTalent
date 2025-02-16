import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import { getAllPublishedOffers } from '@/apiClient';

export const useCandidateJobStore = defineStore('candidateJobs', () => {
  // État des filtres
  const filters = ref({
    search: '',
    contractType: '',
    location: '',
    workMode: '',
    minSalary: 0,
    maxSalary: 150
  });

  const jobOffers = ref([]);
  const loading = ref(false);
  const error = ref(null);

  // Fonction pour charger les offres
  const fetchPublishedOffers = async () => {
    loading.value = true;
    error.value = null;
    try {
      const response = await getAllPublishedOffers();
      console.log('Structure complète des offres reçues:', JSON.stringify(response, null, 2));
      jobOffers.value = response.offers;
    } catch (err) {
      error.value = err.message || 'Erreur lors du chargement des offres';
      console.error('Erreur complète:', err);
    } finally {
      loading.value = false;
    }
  };


  const filteredOffers = computed(() => {
    console.log('Début du filtrage des offres');
    console.log('Offres disponibles:', jobOffers.value);
    console.log('Filtres actuels:', filters.value);
  
    return jobOffers.value.filter(offer => {
      console.log('Vérification de l\'offre:', offer);
  
      // Vérification de la recherche
      const matchSearch = !filters.value.search || 
        offer.title?.toLowerCase().includes(filters.value.search.toLowerCase()) ||
        offer.shortDescription?.toLowerCase().includes(filters.value.search.toLowerCase());
      console.log('matchSearch:', matchSearch);
  
      // Vérification du type de contrat
      const matchContract = !filters.value.contractType || 
        offer.contractType === filters.value.contractType;
      console.log('matchContract:', matchContract);
  
      // Vérification de la localisation
      const matchLocation = !filters.value.location || 
        offer.location?.toLowerCase().includes(filters.value.location.toLowerCase());
      console.log('matchLocation:', matchLocation);
  
      // Vérification du mode de travail
      const matchWorkMode = !filters.value.workMode || 
        offer.workMode === filters.value.workMode;
      console.log('matchWorkMode:', matchWorkMode);
  
      // Vérification du salaire
      const matchSalary = (!offer.salary) || 
        (offer.salary >= filters.value.minSalary && 
         offer.salary <= filters.value.maxSalary);
      console.log('matchSalary:', matchSalary);
  
      const matches = matchSearch && matchContract && matchLocation && 
        matchWorkMode && matchSalary;
      console.log('Résultat final pour cette offre:', matches);
  
      return matches;
    });
  });


  // Getters pour les options de filtres
  const allLocations = computed(() => 
    [...new Set(jobOffers.value.map(offer => offer.location))]
  );

  const allContractTypes = computed(() => 
    [...new Set(jobOffers.value.map(offer => offer.contractType))]
  );

  const allWorkModes = computed(() => 
    [...new Set(jobOffers.value.map(offer => offer.workMode))]
  );

  // Actions
  const updateFilters = (newFilters) => {
    filters.value = { ...filters.value, ...newFilters };
  };

  const resetFilters = () => {
    filters.value = {
      search: '',
      contractType: '',
      location: '',
      workMode: '',
      minSalary: 0,
      maxSalary: 150
    };
  };

  return {
    filters,
    jobOffers,
    loading,
    error,
    filteredOffers,
    allLocations,
    allContractTypes,
    allWorkModes,
    updateFilters,
    resetFilters,
    fetchPublishedOffers
  };

});