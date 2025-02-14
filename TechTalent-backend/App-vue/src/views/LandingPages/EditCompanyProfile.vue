<template>
  <div class="edit-profile-page">
    <div v-if="isLoading" class="loading">
      Chargement...
    </div>
    <div class="edit-container">
      <section class="py-4"></section>
      <div class="header-center">
        <h3>Modifier le Profil de l'Entreprise</h3>
        <h6>Modifier les informations de votre entreprise</h6>
      </div>

      <section class="py-4"></section>
      <form @submit.prevent="handleFormSubmit">
        <div class="form-sections">
          <div class="form-section-left">
            <div class="form-group">
              <h4>Informations de la Société</h4>
            </div>
            <div class="form-group">
              <label>Nom de la société</label>
              <input type="text" class="text-btn" v-model="formData.companyName" />
              <span v-if="errors.companyName" class="error">{{ errors.companyName }}</span>
            </div>

            <div class="form-group">
              <label>Secteur d'activité</label>
              <input type="text" class="text-btn" v-model="formData.sector" />
              <span v-if="errors.sector" class="error">{{ errors.sector }}</span>
            </div>

            <div class="form-group">
              <label>Site Web</label>
              <input type="text" class="text-btn" v-model="formData.website" />
              <span v-if="errors.website" class="error">{{ errors.website }}</span>
            </div>

            <div class="form-group">
              <label>Numéro de téléphone</label>
              <input type="text" class="text-btn" v-model="formData.phoneNumber" />
              <span v-if="errors.phoneNumber" class="error">{{ errors.phoneNumber }}</span>
            </div>

            <div class="form-group">
              <label>Adresse</label>
              <input type="text" class="text-btn" v-model="formData.address" />
              <span v-if="errors.address" class="error">{{ errors.address }}</span>
            </div>
          </div>

          <div class="form-section-right">
            <section class="py-4"></section>
            <section class="py-1"></section>
            <div class="form-group">
              <label>Description</label>
              <textarea class="text-btn description-area" v-model="formData.description"></textarea>
            </div>

            <div class="form-group">
              <label>Taille de l'entreprise</label>
              <input type="text" class="text-btn" v-model="formData.companySize" />
              <span v-if="errors.companySize" class="error">{{ errors.companySize }}</span>
            </div>

            <div class="form-group">
              <label>Année de création</label>
              <input type="text" class="text-btn" v-model="formData.creationYear" />
              <span v-if="errors.creationYear" class="error">{{ errors.creationYear }}</span>
            </div>

            <div class="form-group">
              <label>Logo de la société</label>
              <div class="logo-preview" v-if="formData.companyLogo">
                <img :src="formData.companyLogo" alt="Logo actuel" />
              </div>
              <input type="file" id="company-logo" class="custom-file-input" @change="(e) => handleFileUpload(e, 'companyLogo')" accept="image/*" />
              <label for="company-logo">Choisir un fichier</label>
            </div>
          </div>
        </div>

        <div class="buttons-container">
          <button type="button" @click="handleCancel" class="cancel-button">Annuler</button>
          <button type="button" @click="confirmSave" class="save-button">Sauvegarder</button>
        </div>
      </form>
    </div>

    <!-- Modal de confirmation -->
    <div class="modal" v-if="showConfirmModal">
      <div class="modal-content">
        <h4>Confirmer les modifications</h4>
        <p>Êtes-vous sûr de vouloir sauvegarder ces modifications ?</p>
        <div class="modal-buttons">
          <button @click="showConfirmModal = false" class="cancel-button">Annuler</button>
          <button @click="saveChanges" class="confirm-button">Confirmer</button>
        </div>
      </div>
    </div>
  </div>
  <DefaultFooter />
</template>

<script setup>
import { ref, reactive, onMounted } from "vue";
import { useRouter } from 'vue-router';
import DefaultFooter from "./footers/FooterDefault.vue";
import { getCompanyProfile, updateProfilecompany } from '@/apiClient'; // Ajout de l'import manquant

const router = useRouter();
const showConfirmModal = ref(false);
const isLoading = ref(true); // Commencer avec loading=true

const formData = reactive({
  companyName: "",
  companyLogo: "",
  sector: "",
  description: "",
  website: "",
  phoneNumber: "",
  address: "",
  companySize: "",
  creationYear: "",
});

const errors = reactive({});

onMounted(async () => {
  try {
    console.log('Chargement du profil...');
    const response = await getCompanyProfile();
    console.log('Données reçues:', response);
    
    // Mise à jour directe des champs
    formData.companyName = response.companyName || '';
    formData.sector = response.sector || '';
    formData.description = response.description || '';
    formData.website = response.website || '';
    formData.phoneNumber = response.phoneNumber || '';
    formData.address = response.address || '';
    formData.companySize = response.companySize || '';
    formData.creationYear = response.creationYear || '';
    formData.companyLogo = response.companyLogo || '';
    
  } catch (error) {
    console.error('Erreur lors du chargement des données:', error);
  } finally {
    isLoading.value = false;
  }
});


const handleFileUpload = (event, key) => {
  const file = event.target.files[0];
  if (file) {
    formData[key] = file; // Stocker le fichier lui-même
    
    // Créer une URL pour la prévisualisation
    const reader = new FileReader();
    reader.onload = (e) => {
      formData[`${key}Preview`] = e.target.result;
    };
    reader.readAsDataURL(file);
  }
};

const handleCancel = () => {
  router.push('/dashboard');
};

const confirmSave = () => {
  if (!formData.companyName || !formData.sector) {
    alert("Veuillez remplir tous les champs obligatoires");
    return;
  }
  showConfirmModal.value = true;
};

const saveChanges = async () => {
  try {
    isLoading.value = true; // Utiliser isLoading au lieu de loading
    const form = new FormData();
    Object.keys(formData).forEach((key) => {
      if (formData[key]) {
        form.append(key, formData[key]);
      }
    });
    await updateProfilecompany(form);
    showConfirmModal.value = false;
    router.push('/dashboard');
  } catch (error) {
    console.error('Erreur lors de la sauvegarde:', error);
    alert("Une erreur est survenue lors de la sauvegarde");
  } finally {
    isLoading.value = false; // Utiliser isLoading au lieu de loading
  }
};

</script>

<style scoped>
.edit-profile-page {
  min-height: 100vh;
  background: #f9fafb;
  padding: 2rem;
}

.edit-container {
  max-width: 1200px;
  margin: 0 auto;
  background: white;
  padding: 2rem;
  border-radius: 0.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.header-center {
  text-align: center;
  margin-bottom: 2rem;
}

.form-sections {
  display: flex;
  gap: 2rem;
}

.form-section-left,
.form-section-right {
  flex: 1;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  font-size: 0.875rem;
  font-weight: 500;
  color: #374151;
  margin-bottom: 0.5rem;
}

.text-btn {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #e5e7eb;
  border-radius: 0.375rem;
  font-size: 0.875rem;
}

.description-area {
  min-height: 100px;
  resize: vertical;
}

.logo-preview {
  margin-bottom: 1rem;
}

.logo-preview img {
  max-width: 150px;
  height: auto;
  border-radius: 0.375rem;
}

.buttons-container {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  margin-top: 2rem;
}

.save-button,
.cancel-button {
  padding: 0.75rem 1.5rem;
  border-radius: 0.375rem;
  font-weight: 500;
  cursor: pointer;
}

.save-button {
  background-color: #5d6c8d;
  color: white;
  border: none;
}

.cancel-button {
  background-color: #ffffff;
  color: #374151;
  border: 1px solid #d1d5db;
}

.save-button:hover {
  background-color: #4a5578;
}

.cancel-button:hover {
  background-color: #f9fafb;
}

/* Modal styles */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background-color: white;
  padding: 2rem;
  border-radius: 0.5rem;
  max-width: 500px;
  width: 90%;
}

.modal-buttons {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  margin-top: 1.5rem;
}

.confirm-button {
  background-color: #5d6c8d;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0.375rem;
  cursor: pointer;
}

.confirm-button:hover {
  background-color: #4a5578;
}

.custom-file-input {
width: 0.1px;
height: 0.1px;
opacity: 0;
overflow: hidden;
position: absolute;
z-index: -1;
}

.custom-file-input + label {
background-color: #5d6c8d;
color: white;
padding: 0.75rem 1.5rem;
border-radius: 0.375rem;
display: inline-block;
cursor: pointer;
font-size: 0.875rem;
transition: background-color 0.3s ease;
}

.custom-file-input + label:hover {
background-color: #4a5578;
}

/* Cacher le texte "No file chosen" */
input[type="file"]::-webkit-file-upload-button {
display: none;
}

.error {
  color: #dc2626;
  font-size: 0.75rem;
  margin-top: 0.25rem;
}
</style>
