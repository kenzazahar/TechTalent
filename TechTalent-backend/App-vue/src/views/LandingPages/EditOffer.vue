<script setup>
import { ref, reactive, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useJobOffersStore } from '@/stores/jobOffersStore.js';

const router = useRouter();
const route = useRoute();
const jobOffersStore = useJobOffersStore();

const formData = reactive({
  title: "",
  shortDescription: "",
  details: "",
  fullDescription: "",
  requiredSkills: "",
  contractType: "",
  workMode: "",
  location: "",
  offerDuration: "",
  salary: "",
  recruiterName: "",
  recruiterEmail: "",
  recruiterPhone: "",
  offerImage: null,
});

const errors = reactive({});

onMounted(async () => {
  const offerId = parseInt(route.params.id);
  
  // Charger les offres publiées si elles ne sont pas déjà chargées
  if (jobOffersStore.publishedOffers.length === 0) {
    await jobOffersStore.fetchPublishedOffers();
  }

  // Trouver l'offre correspondante
  const offer = jobOffersStore.publishedOffers.find(o => o.id === offerId);
  
  if (!offer) {
    router.push('/dashboard');
    return;
  }

  // Remplir le formulaire avec les données de l'offre
  Object.assign(formData, {
    title: offer.title,
    shortDescription: offer.shortDescription,
    details: offer.details,
    fullDescription: offer.fullDescription,
    requiredSkills: offer.requiredSkills,
    contractType: offer.contractType,
    workMode: offer.workMode,
    location: offer.location,
    offerDuration: offer.offerDuration,
    salary: offer.salary,
    recruiterName: offer.recruiterName,
    recruiterEmail: offer.recruiterEmail,
    recruiterPhone: offer.recruiterPhone,
    offerImage: offer.offerImage,
  });

  console.log("Données du formulaire :", formData); // Debug
});

const validateForm = () => {
  // Réinitialisation des erreurs
  Object.keys(errors).forEach((key) => {
    errors[key] = "";
  });

  if (!formData.title) {
    errors.title = "Le titre est requis.";
    return false;
  }

  if (!formData.shortDescription) errors.shortDescription = "La description courte est requise.";
  if (!formData.details) errors.details = "Les détails sont requis.";
  if (!formData.fullDescription) errors.fullDescription = "La description complète est requise.";
  if (!formData.requiredSkills) errors.requiredSkills = "Les compétences requises sont obligatoires.";
  if (!formData.contractType) errors.contractType = "Le type de contrat est requis.";
  if (!formData.workMode) errors.workMode = "Le mode de travail est requis.";
  if (!formData.recruiterName) errors.recruiterName = "Le nom du recruteur est requis.";
  if (!formData.recruiterEmail) {
    errors.recruiterEmail = "L'email du recruteur est requis.";
  } else if (!/\S+@\S+\.\S+/.test(formData.recruiterEmail)) {
    errors.recruiterEmail = "Format de l'email invalide.";
  }

  return Object.values(errors).every((error) => !error);
};

const handleFileUpload = (event) => {
  const file = event.target.files[0];
  if (file) {
    formData.offerImage = file;
  }
};

const handleSave = async () => {
  console.log("handleSave appelé"); // Debug
  if (!validateForm()) {
    console.log("Validation du formulaire échouée"); // Debug
    return;
  }

  try {
    console.log("Données envoyées :", formData); // Debug
    await jobOffersStore.updatePublishedOffer({
      ...formData,
      id: parseInt(route.params.id)
    });
    router.push({ name: 'PublishOfferDetail', params: { id: route.params.id } });
  } catch (error) {
    console.error('Erreur lors de la mise à jour de l\'offre:', error);
  }
};

const handleCancel = () => {
  router.push('/dashboard');
};
</script>

<template>
  <div class="login-page">
    <div class="login-container">
      <h3>Modifier l'offre</h3>
      <form @submit.prevent="handleSave">
        <div class="form-sections">
          <!-- Partie gauche -->
          <div class="form-section-left">
            <div class="form-group">
              <label>Titre *</label>
              <input type="text" class="text-btn" v-model="formData.title" placeholder="Entrez le titre" />
              <span v-if="errors.title" class="error">{{ errors.title }}</span>
            </div>

            <div class="form-group">
              <label>Description courte *</label>
              <input type="text" class="text-btn" v-model="formData.shortDescription" placeholder="Entrez une description courte" />
              <span v-if="errors.shortDescription" class="error">{{ errors.shortDescription }}</span>
            </div>

            <div class="form-group">
              <label>Détails *</label>
              <input type="text" class="text-btn" v-model="formData.details" placeholder="Entrez les détails" />
              <span v-if="errors.details" class="error">{{ errors.details }}</span>
            </div>

            <div class="form-group">
              <label>Description complète du poste *</label>
              <textarea class="text-btn" v-model="formData.fullDescription" placeholder="Entrez une description complète"></textarea>
              <span v-if="errors.fullDescription" class="error">{{ errors.fullDescription }}</span>
            </div>

            <div class="form-group">
              <label>Compétences requises *</label>
              <textarea class="text-btn" v-model="formData.requiredSkills" placeholder="Entrez les compétences requises"></textarea>
              <span v-if="errors.requiredSkills" class="error">{{ errors.requiredSkills }}</span>
            </div>

            <div class="form-group">
              <label>Type de contrat *</label>
              <select class="text-btn" v-model="formData.contractType">
                <option value="">Sélectionnez le type de contrat</option>
                <option value="CDI">CDI</option>
                <option value="CDD">CDD</option>
                <option value="Freelance">Freelance</option>
              </select>
              <span v-if="errors.contractType" class="error">{{ errors.contractType }}</span>
            </div>

            <div class="form-group">
              <label>Mode de travail *</label>
              <select class="text-btn" v-model="formData.workMode">
                <option value="">Sélectionnez le mode de travail</option>
                <option value="Présentiel">Présentiel</option>
                <option value="Télétravail">Télétravail</option>
                <option value="Hybride">Hybride</option>
              </select>
              <span v-if="errors.workMode" class="error">{{ errors.workMode }}</span>
            </div>
          </div>

          <!-- Partie droite -->
          <div class="form-section-right">
            <div class="form-group">
              <label>Localisation</label>
              <input type="text" class="text-btn" v-model="formData.location" placeholder="Entrez la localisation" />
            </div>

            <div class="form-group">
              <label>Durée de l'offre</label>
              <input type="text" class="text-btn" v-model="formData.offerDuration" placeholder="Entrez la durée de l'offre" />
            </div>

            <div class="form-group">
              <label>Salaire</label>
              <input type="text" class="text-btn" v-model="formData.salary" placeholder="Entrez le salaire" />
            </div>

            <div class="form-group">
              <label>Nom du recruteur *</label>
              <input type="text" class="text-btn" v-model="formData.recruiterName" placeholder="Entrez le nom du recruteur" />
              <span v-if="errors.recruiterName" class="error">{{ errors.recruiterName }}</span>
            </div>

            <div class="form-group">
              <label>Email du recruteur *</label>
              <input type="email" class="text-btn" v-model="formData.recruiterEmail" placeholder="Entrez l'email du recruteur" />
              <span v-if="errors.recruiterEmail" class="error">{{ errors.recruiterEmail }}</span>
            </div>

            <div class="form-group">
              <label>Téléphone du recruteur</label>
              <input type="text" class="text-btn" v-model="formData.recruiterPhone" placeholder="Entrez le téléphone du recruteur" />
            </div>

            <div class="form-group">
              <label>Image de l'offre</label>
              <input type="file" class="custom-file-input" @change="handleFileUpload" accept="image/*" />
            </div>
          </div>
        </div>

        <!-- Boutons d'action -->
        <div class="form-actions">
          <button type="button" class="cancel-button" @click="handleCancel">Annuler</button>
          <button type="submit" class="submit-button">Enregistrer les modifications</button>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped>
.login-page {
    display: flex;
    justify-content: center;
    align-items: center;
    height: auto;
  }

  .login-container {
    width: 100%;
    max-width: 1200px;
    background: #fff;
    padding: 50px;
    border-radius: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }

  .form-sections {
    display: flex;
    justify-content: space-between;
    gap: 20px;
  }

  .form-section-left, .form-section-right {
    width: 48%;
  }

  .form-group {
    margin-bottom: 20px;
    text-align: left;
  }

  .form-group label {
    font-size: 16px;
    display: block;
    margin-bottom: 5px;
  }

  .form-group input, .form-group textarea, .form-group select {
    width: 100%;
    padding: 10px;
    margin-top: 5px;
    border: 1px solid #ccc;
    border-radius: 10px;
    font-size: 14px;
  }

  .form-actions {
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
  }

  .cancel-button, .draft-button, .submit-button {
    padding: 10px 20px;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    font-size: 16px;
  }

  .cancel-button {
    background: #575555;
    color: #fff;
  }
  .cancel-button:hover {
    background: #2e2c2c;
    color: #fff;
  }

  .draft-button {
    background: #272629;
    color: #fff;
  }

  .submit-button {
    background: #12101d;
    color: #fff;
  }
  .submit-button:hover {
    background: #050506;
    color: #fff;
  }


  .error {
    color: rgb(142, 22, 22);
    font-size: 12px;
    margin-top: 5px;
  }

  .custom-file-input {
    position: relative;
    display: inline-block;
  }

  .custom-file-input::before {
    content: "Choisir un fichier";
    display: inline-block;
    background-color: #5d6c8d;
    color: white;
    border: none;
    padding: 5px 20px;
    border-radius: 5px;
    cursor: pointer;
  }

  .custom-file-input:hover::before {
    background-color: #42668b;
  }

  .custom-file-input:active::before {
    background-color: #4c79a7;
  }

  .custom-file-input::-webkit-file-upload-button {
    visibility: hidden;
  }
</style>