import { defineStore } from 'pinia';
import { createJobOffer, getPublishedOffers, getDraftOffers, updateJobOffer, deleteJobOffer } from '@/apiClient';

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
        console.log("Offres publiées chargées :", this.publishedOffers); // Debug
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
    },

    async deletePublishedOffer(offerId) {
      this.loading = true;
      this.error = null;
      try {
        await deleteJobOffer(offerId);
        this.publishedOffers = this.publishedOffers.filter(offer => offer.id !== offerId);
      } catch (error) {
        this.error = error.message || 'Une erreur est survenue lors de la suppression';
        throw error;
      } finally {
        this.loading = false;
      }
    },

    async updatePublishedOffer(updatedOffer) {
      this.loading = true;
      this.error = null;
      try {
        console.log("Mise à jour de l'offre :", updatedOffer); // Debug
        const response = await updateJobOffer(updatedOffer.id, updatedOffer);
        console.log("Réponse de l'API :", response); // Debug

        const index = this.publishedOffers.findIndex(offer => offer.id === updatedOffer.id);
        if (index !== -1) {
          this.publishedOffers[index] = response;
        }
      } catch (error) {
        this.error = error.message || 'Une erreur est survenue lors de la mise à jour';
        throw error;
      } finally {
        this.loading = false;
      }
    },

    async updateDraft({ id, ...formData }) {
      this.loading = true;
      try {
        console.log("Données envoyées pour la mise à jour :", formData); // Debug
        const response = await updateJobOffer(id, formData);
        console.log("Réponse de l'API :", response); // Debug

        const index = this.draftOffers.findIndex(offer => offer.id === id);
        if (index !== -1) {
          this.draftOffers[index] = response;
        }
        return response;
      } catch (error) {
        console.error("Erreur lors de la mise à jour du brouillon :", error); // Debug
        this.error = error.message || 'Erreur lors de la mise à jour du brouillon';
        throw error;
      } finally {
        this.loading = false;
      }
    },

    async publishDraft(id) {
      this.loading = true;
      try {
        console.log("Publication du brouillon avec ID :", id); // Debug
        const response = await updateJobOffer(id, { isPublish: true });
        console.log("Réponse de l'API :", response); // Debug

        const index = this.draftOffers.findIndex(offer => offer.id === id);
        if (index !== -1) {
          this.draftOffers.splice(index, 1); // Retirer du tableau des brouillons
          this.publishedOffers.push(response); // Ajouter aux offres publiées
        }
        return response;
      } catch (error) {
        console.error("Erreur lors de la publication du brouillon :", error); // Debug
        this.error = error.message || 'Erreur lors de la publication du brouillon';
        throw error;
      } finally {
        this.loading = false;
      }
    },

    async deleteDraft(id) {
      this.loading = true;
      try {
        await deleteJobOffer(id);
        this.draftOffers = this.draftOffers.filter(offer => offer.id !== id);
      } catch (error) {
        this.error = error.message || 'Erreur lors de la suppression du brouillon';
        throw error;
      } finally {
        this.loading = false;
      }
    },
  }
});