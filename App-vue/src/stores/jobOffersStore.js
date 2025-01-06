
import { ref, computed } from 'vue';
import { defineStore } from 'pinia';

export const useJobOffersStore = defineStore('jobOffers', () => {
  const publishedOffers = ref([
    {
      id: 1,
      title: "Développeur Full Stack",
      location: "CDI - Paris",
      image: "/src/assets/img/full.jpg"
    },
    {
      id: 2,
      title: "Ingénieur DevOps",
      location: "CDI - Lyon",
      image: "/src/assets/img/DevOps-Cest-quoi-par-Qim-info.jpg"
    },
    {
      id: 3,
      title: "Data Scientist",
      location: "Freelance - Marseille",
      image: "/src/assets/img/ds.jpg"
    },
    {
      id: 10,
      title: "Développeur Mobile",
      location: "Freelance - Lyon",
      image: "/src/assets/img/mobile.jpg"
    },
    {
      id: 12,
      title: "Testeur QA",
      location: "Stage - Strasbourg",
      image: "/src/assets/img/teste.jpg"
    },
    {
      id: 13,
      title: "Responsable Sécurité Informatique",
      location: "CDI - Montpellier",
      image: "/src/assets/img/secur.jpg"
    },
    {
      id: 14,
      title: "Développeur Backend",
      location: "Freelance - Grenoble",
      image: "/src/assets/img/back.jpg"
    },
    {
      id: 16,
      title: "Scrum Master",
      location: "CDI - Marseille",
      image: "/src/assets/img/scrum.jpg"
    }
  ]);

  const draftOffers = ref([
    {
      id: 5,
      title: "Consultant en Cybersécurité",
      location: "Stage - Lille",
      image: "/src/assets/img/cybersecurite.jpg"
    },
    {
      id: 6,
      title: "Développeur Front-End",
      location: "CDI - Toulouse",
      image: "/src/assets/img/front.jpg"
    },
    {
      id: 7,
      title: "Architecte Cloud",
      location: "Freelance - Nantes",
      image: "/src/assets/img/cloud.jpg"
    },
    {
      id: 8,
      title: "Ingénieur Réseaux",
      location: "CDI - Nice",
      image: "/src/assets/img/reseau.jpg"
    }
        
  ]);
  // Ajouter/Modifier les fonctions suivantes

  // Mettre à jour un brouillon existant
  const updateDraft = (updatedDraft) => {
    const index = draftOffers.value.findIndex(d => d.id === updatedDraft.id);
    if (index !== -1) {
      // Créer une nouvelle offre avec les données mises à jour
      const updatedOffer = {
        ...draftOffers.value[index],
        ...updatedDraft,
        location: `${updatedDraft.contractType} - ${updatedDraft.location || 'Non spécifié'}`,
        image: updatedDraft.offerImage 
          ? URL.createObjectURL(updatedDraft.offerImage) 
          : draftOffers.value[index].image
      };
      draftOffers.value[index] = updatedOffer;
    }
  };

  // Supprimer un brouillon
  const deleteDraft = (id) => {
    const index = draftOffers.value.findIndex(d => d.id === id);
    if (index !== -1) {
      draftOffers.value.splice(index, 1);
    }
  };

  // Publier un brouillon (le déplacer vers les offres publiées)
  const publishDraft = (draftId) => {
    const draft = draftOffers.value.find(d => d.id === draftId);
    if (draft) {
      // Ajouter aux offres publiées
      const publishedOffer = {
        ...draft,
        id: getNewId(),
        publishedAt: new Date().toISOString()
      };
      publishedOffers.value.push(publishedOffer);
      
      // Supprimer des brouillons
      deleteDraft(draftId);
    }
  };

  const deletePublishedOffer = (id) => {
    const index = publishedOffers.value.findIndex(o => o.id === id);
    if (index !== -1) {
      publishedOffers.value.splice(index, 1);
    }
  };
  
  const updatePublishedOffer = (updatedOffer) => {
    const index = publishedOffers.value.findIndex(o => o.id === updatedOffer.id);
    if (index !== -1) {
      publishedOffers.value[index] = { ...updatedOffer };
    }
  };
  

  // Helper to generate new ID
  const getNewId = () => {
    const allIds = [...publishedOffers.value.map(o => o.id), ...draftOffers.value.map(o => o.id)];
    return Math.max(...allIds) + 1;
  };

  // Add new draft offer
  const addDraft = (offerData) => {
    const newOffer = {
      id: getNewId(),
      ...offerData,
      location: `${offerData.contractType} - ${offerData.location || 'Non spécifié'}`,
      image: offerData.offerImage ? URL.createObjectURL(offerData.offerImage) : '/src/assets/img/default-offer.jpg'
    };
    draftOffers.value.push(newOffer);
  };

  // Add new published offer
  const addPublishedOffer = (offerData) => {
    const newOffer = {
      id: getNewId(),
      ...offerData,
      location: `${offerData.contractType} - ${offerData.location || 'Non spécifié'}`,
      image: offerData.offerImage ? URL.createObjectURL(offerData.offerImage) : '/src/assets/img/default-offer.jpg'
    };
    publishedOffers.value.push(newOffer);
  };

  return {
    publishedOffers,
    draftOffers,
    addDraft,
    addPublishedOffer,
    deletePublishedOffer,
    updatePublishedOffer,
    updateDraft, // Nouvelle fonction
    deleteDraft, // Nouvelle fonction
    publishDraft  
  };
});