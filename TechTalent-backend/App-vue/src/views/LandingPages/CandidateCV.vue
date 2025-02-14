<!-- src/views/LandingPages/CandidateCV.vue -->
<template>
    <div class="cv-container">
      <div class="cv-content">
        <h1>CV de {{ candidate?.firstName }} {{ candidate?.lastName }}</h1>
        <!-- Ici nous afficherons le contenu du CV -->
        <div v-if="cv" v-html="cv" class="cv-details"></div>
        <div v-else class="cv-loading">Chargement du CV...</div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute } from 'vue-router';
  
  const route = useRoute();
  const candidate = ref(null);
  const cv = ref(null);
  
  onMounted(async () => {
    // Ici vous ferez un appel API pour récupérer les détails du CV
    // Pour l'exemple, on utilisera des données statiques
    const candidateId = route.params.id;
    // Simuler un appel API
    try {
      // Remplacer ceci par votre véritable appel API
      const response = await fetch(`/api/candidates/${candidateId}/cv`);
      const data = await response.json();
      candidate.value = data.candidate;
      cv.value = data.cv;
    } catch (error) {
      console.error('Erreur lors du chargement du CV:', error);
    }
  });
  </script>
  
<style scoped>
  .cv-container {
    padding: 2rem;
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .cv-content {
    background: white;
    padding: 2rem;
    border-radius: 0.5rem;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  }
  
  .cv-details {
    margin-top: 2rem;
  }
  
  .cv-loading {
    text-align: center;
    padding: 2rem;
    color: #666;
  }
</style>