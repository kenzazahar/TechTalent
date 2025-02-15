import { defineStore } from 'pinia';
import { createJobOffer, getPublishedOffers, getDraftOffers, updateJobOffer } from '@/apiClient';

export const useJobOffersStore = defineStore('jobOffers', {
  state: () => ({
    publishedOffers: [],
    draftOffers: [],
    loading: false,
    error: null
  }),

  actions: {
    async createOffer(formData, isPublish) {
      this.loading = true;
      this.error = null;
      try {
        const response = await createJobOffer(formData, isPublish);
        const newOffer = response;
    
        // Ajouter l'offre à la bonne liste selon son statut
        if (isPublish) {
          this.publishedOffers.push(newOffer);
        } else {
          this.draftOffers.push(newOffer);
        }
    
        return true;
      } catch (error) {
        this.error = error.message || 'Une erreur est survenue';
        throw error;
      } finally {
        this.loading = false;
      }
    },

    async fetchPublishedOffers() {
      this.loading = true;
      try {
        const response = await getPublishedOffers();
        this.publishedOffers = response.offers;
      } catch (error) {
        this.error = error.message || 'Erreur lors du chargement des offres publiées';
        throw error;
      } finally {
        this.loading = false;
      }
    },

    async fetchDraftOffers() {
      this.loading = true;
      try {
        const response = await getDraftOffers();
        this.draftOffers = response.offers;
      } catch (error) {
        this.error = error.message || 'Erreur lors du chargement des brouillons';
        throw error;
      } finally {
        this.loading = false;
      }
    },

    async updateOffer(id, formData) {
      this.loading = true;
      try {
        await updateJobOffer(id, formData);
        // Vérifier si l'offre est maintenant publiée ou toujours en brouillon et mettre à jour les listes
        await Promise.all([this.fetchPublishedOffers(), this.fetchDraftOffers()]);
      } catch (error) {
        this.error = error.message || 'Erreur lors de la mise à jour';
        throw error;
      } finally {
        this.loading = false;
      }
    }
  }
});
