<script setup>
import { ref, reactive, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useJobOffersStore } from '@/stores/jobOffersStore';
import DefaultFooter from "./footers/FooterDefault.vue";

const router = useRouter();
const route = useRoute();
const jobOffersStore = useJobOffersStore();

const showConfirmDialog = ref(false);

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

onMounted(() => {
  const offerId = parseInt(route.params.id);
  const draft = jobOffersStore.draftOffers.find(d => d.id === offerId);
  
  if (!draft) {
    router.push('/dashboard');
    return;
  }

  // Remplir le formulaire avec les données du brouillon
  Object.assign(formData, draft);
});

const validateForm = (isPublish = false) => {
  // Réinitialisation des erreurs
  Object.keys(errors).forEach((key) => {
    errors[key] = "";
  });

  // Validation basique pour la sauvegarde comme brouillon
  if (!formData.title) {
    errors.title = "Le titre est requis.";
    return false;
  }

  // Validations supplémentaires pour la publication
  if (isPublish) {
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
  }

  return Object.values(errors).every((error) => !error);
};

const handleFileUpload = (event) => {
  const file = event.target.files[0];
  if (file) {
    formData.offerImage = file;
  }
};

const saveDraft = () => {
  if (!validateForm()) {
    return;
  }

  jobOffersStore.updateDraft({
    ...formData,
    id: parseInt(route.params.id)
  });
  
  router.push('/dashboard');
};

const publishOffer = () => {
  if (!validateForm(true)) {
    return;
  }

  const offerId = parseInt(route.params.id);
  
  jobOffersStore.publishDraft(offerId);
  router.push('/dashboard');
};

const confirmDelete = () => {
  showConfirmDialog.value = true;
};

const handleDelete = () => {
  const offerId = parseInt(route.params.id);
  jobOffersStore.deleteDraft(offerId);
  showConfirmDialog.value = false;
  router.push('/dashboard');
};

const cancelDelete = () => {
  showConfirmDialog.value = false;
};

const handleCancel = () => {
  router.push('/dashboard');
};
</script>

<template>
  <div class="login-page">
    <div class="login-container">
      <h3>Modifier le brouillon</h3>
      <form @submit.prevent="publishOffer">
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

            <!-- [Autres champs de gauche identiques à EditOffer.vue] -->
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
            <!-- [Champs de droite identiques à EditOffer.vue] -->
          </div>
        </div>

        <!-- Boutons d'action -->
        <div class="form-actions">
          
          <button type="button" class="draft-button" @click="saveDraft">Sauvegarder comme brouillon</button>
          <button type="submit" class="submit-button">Publier</button>
          <button type="button" class="delete-button" @click="confirmDelete">Supprimer</button>
          <button type="button" class="cancel-button" @click="handleCancel">Annuler</button>
          
        </div>
      </form>
    </div>

    <!-- Dialog de confirmation de suppression -->
    <div v-if="showConfirmDialog" class="confirm-dialog">
      <div class="confirm-dialog-content">
        <h4>Confirmer la suppression</h4>
        <p>Êtes-vous sûr de vouloir supprimer ce brouillon ?</p>
        <div class="confirm-dialog-actions">
          <button class="cancel-button" @click="cancelDelete">Annuler</button>
          <button class="delete-button" @click="handleDelete">Supprimer</button>
        </div>
      </div>
    </div>
  </div>

  <DefaultFooter />
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
  .draft-button:hover{
    background: #0d0d0f;
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

.delete-button {
  background: #310307;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  font-size: 16px;
}

.delete-button:hover {
  background: #130204;
}

.confirm-dialog {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.confirm-dialog-content {
  background: white;
  padding: 20px;
  border-radius: 10px;
  width: 400px;
  text-align: center;
}

.confirm-dialog-actions {
  display: flex;
  justify-content: space-around;
  margin-top: 20px;
}
</style>