import { ref, computed } from 'vue';
import { defineStore } from 'pinia';

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

  // Liste des offres (utilisant les mêmes données que le store entreprise)
  const jobOffers = ref([
    {
        id: 14,
        title: "Développeur Backend",
        location: "Grenoble",
        contractType: "Freelance",
        workMode: "Télétravail",
        salary: 52,
        image: "/src/assets/img/back.jpg",
        description: "Développement de microservices et APIs REST",
        tags: ["Java", "Spring Boot", "PostgreSQL"]
      },
  
    {
      id: 2,
      title: "Ingénieur DevOps",
      location: "Lyon",
      contractType: "CDI",
      workMode: "Hybride",
      salary: 50,
      image: "/src/assets/img/DevOps-Cest-quoi-par-Qim-info.jpg",
      description: "Venez renforcer notre équipe DevOps et améliorer nos processus de déploiement",
      tags: ["Docker", "Kubernetes", "AWS"]
    },
    {
      id: 3,
      title: "Data Scientist",
      location: "Marseille",
      contractType: "Freelance",
      workMode: "Télétravail",
      salary: 65,
      image: "/src/assets/img/ds.jpg",
      description: "Mission passionnante dans l'analyse de données et le machine learning",
      tags: ["Python", "Machine Learning", "SQL"]
    },
    
    
    {
      id: 13,
      title: "Responsable Sécurité Informatique",
      location: "Montpellier",
      contractType: "CDI",
      workMode: "Sur site",
      salary: 60,
      image: "/src/assets/img/secur.jpg",
      description: "Prenez en charge la sécurité de notre infrastructure IT",
      tags: ["Cybersécurité", "CISSP", "Pentest"]
    },
    
    {
      id: 16,
      title: "Scrum Master",
      location: "Marseille",
      contractType: "CDI",
      workMode: "Hybride",
      salary: 48,
      image: "/src/assets/img/scrum.jpg",
      description: "Accompagnez nos équipes dans leur transformation agile",
      tags: ["Agile", "Scrum", "Kanban", "Jira"]
    },
    {
        id: 1,
        title: "Développeur Full Stack",
        location: "Paris",
        contractType: "CDI",
        workMode: "Hybride",
        salary: 45,
        image: "/src/assets/img/full.jpg",
        description: "Rejoignez notre équipe dynamique pour développer des applications web innovantes",
        tags: ["Vue.js", "Node.js", "MongoDB"]
      },
      {
        id: 12,
        title: "Testeur QA",
        location: "Strasbourg",
        contractType: "Stage",
        workMode: "Sur site",
        salary: 25,
        image: "/src/assets/img/teste.jpg",
        description: "Stage en assurance qualité logicielle au sein d'une équipe agile",
        tags: ["Selenium", "Cypress", "Jest"]
      },
      {
        id: 10,
        title: "Développeur Mobile",
        location: "Lyon",
        contractType: "Freelance",
        workMode: "Hybride",
        salary: 55,
        image: "/src/assets/img/mobile.jpg",
        description: "Développement d'applications mobiles innovantes pour nos clients",
        tags: ["React Native", "iOS", "Android"]
      }
     

]);

  // Computed property pour les offres filtrées
  const filteredOffers = computed(() => {
    return jobOffers.value.filter(offer => {
      const matchSearch = !filters.value.search || 
        offer.title.toLowerCase().includes(filters.value.search.toLowerCase()) ||
        offer.description.toLowerCase().includes(filters.value.search.toLowerCase());
        
      const matchContract = !filters.value.contractType || 
        offer.contractType === filters.value.contractType;
        
      const matchLocation = !filters.value.location || 
        offer.location === filters.value.location;
        
      const matchWorkMode = !filters.value.workMode || 
        offer.workMode === filters.value.workMode;
        
      const matchSalary = offer.salary >= filters.value.minSalary && 
        offer.salary <= filters.value.maxSalary;

      return matchSearch && matchContract && matchLocation && 
        matchWorkMode && matchSalary;
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
    filteredOffers,
    allLocations,
    allContractTypes,
    allWorkModes,
    updateFilters,
    resetFilters
  };
});