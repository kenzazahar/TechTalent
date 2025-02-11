<template>
  <div class="edit-profile-page">
    <div v-if="loading" class="loading-overlay">
      <div class="loading-spinner">Chargement...</div>
    </div>
    <div class="edit-container">
      <section class="py-4"></section>
      <div class="header-center">
        <h3>Modifier le Profil de l'Entreprise</h3>
        <h6>Modifier les informations de votre entreprise</h6>
      </div>

      <section class="py-4"></section>
      <form @submit.prevent="confirmSave">
        <div class="form-sections">
          <div class="form-section-left">
            <div class="form-group">
              <h4>Informations Générales</h4>
            </div>
            <div class="form-group">
              <label>Nom de l'Entreprise</label>
              <input type="text" class="text-btn" v-model="formData.companyName" />
              <span v-if="errors.companyName" class="error">{{ errors.companyName }}</span>
            </div>

            <div class="form-group">
              <label>Secteur d'Activité</label>
              <input type="text" class="text-btn" v-model="formData.sector" />
            </div>

            <div class="form-group">
              <label>Description</label>
              <textarea class="text-btn" v-model="formData.description"></textarea>
            </div>

            <div class="form-group">
              <label>Site Web</label>
              <input type="url" class="text-btn" v-model="formData.website" />
            </div>
          </div>

          <div class="form-section-right">
            <div class="form-group">
              <h4>Contact</h4>
            </div>
            <div class="form-group">
              <label>Numéro de Téléphone</label>
              <input type="text" class="text-btn" v-model="formData.phoneNumber" />
            </div>

            <div class="form-group">
              <label>Adresse</label>
              <input type="text" class="text-btn" v-model="formData.address" />
            </div>
          </div>
        </div>

        <div class="form-group">
          <label>Logo</label>
          <div class="photo-preview" v-if="formData.logo">
            <img :src="formData.logo" alt="Logo actuel" />
          </div>
          <input type="file" id="company-logo" class="custom-file-input" @change="handleFileUpload($event, 'logo')" accept="image/*" />
          <label for="company-logo">Choisir un logo</label>
        </div>

        <div class="buttons-container">
          <button type="button" @click="handleCancel" class="cancel-button">Annuler</button>
          <button type="submit" class="save-button">Sauvegarder</button>
        </div>
      </form>
    </div>

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
</template>

<script setup>
import { ref, reactive, onMounted } from "vue";
import { useRouter } from "vue-router";
import { getCompanyProfile, updateCompanyProfile } from "@/apiClient";

const router = useRouter();
const showConfirmModal = ref(false);
const loading = ref(false);

const formData = reactive({
  companyName: "",
  sector: "",
  description: "",
  website: "",
  phoneNumber: "",
  address: "",
  logo: null,
});

const errors = reactive({});

onMounted(async () => {
  try {
    loading.value = true;
    const profileData = await getCompanyProfile();
    Object.keys(profileData).forEach((key) => {
      if (formData.hasOwnProperty(key)) {
        formData[key] = profileData[key];
      }
    });
  } catch (error) {
    console.error("Erreur lors du chargement des données:", error);
  } finally {
    loading.value = false;
  }
});

const handleFileUpload = (event, key) => {
  const file = event.target.files[0];
  if (file) {
    formData[key] = file;
  }
};

const handleCancel = () => {
  router.push("/company/dashboard");
};

const validateForm = () => {
  const newErrors = {};
  if (!formData.companyName) newErrors.companyName = "Le nom de l'entreprise est requis";
  Object.assign(errors, newErrors);
  return Object.keys(newErrors).length === 0;
};

const confirmSave = () => {
  if (validateForm()) {
    showConfirmModal.value = true;
  }
};

const saveChanges = async () => {
  try {
    loading.value = true;
    const form = new FormData();
    Object.keys(formData).forEach((key) => {
      if (formData[key]) {
        form.append(key, formData[key]);
      }
    });
    await updateCompanyProfile(form);
    router.push("/company/dashboard");
  } catch (error) {
    console.error("Erreur lors de la sauvegarde:", error);
  } finally {
    loading.value = false;
  }
};
</script>
    
<style scoped>
  .page-layout {
    display: flex;
    min-height: 100vh;
  }
  
  .main-content {
    flex: 1;
    margin-left: 260px;
    padding: 2rem;
    background: #f9fafb;
    min-height: 100vh;
  }
  
  .container {
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .profile-card {
    background: white;
    border-radius: 0.5rem;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    padding: 2rem;
  }
  
  .profile-header {
    text-align: center;
    margin-bottom: 2rem;
  }
  
  .company-logo {
    width: 120px;
    height: 120px;
    object-fit: contain;
    margin-bottom: 1rem;
  }
  
  .company-name {
    font-size: 1.5rem;
    color: #111827;
    margin: 0;
  }
  
  .profile-sections {
    display: grid;
    gap: 2rem;
  }
  
  .profile-section {
    border-bottom: 1px solid #e5e7eb;
    padding-bottom: 1.5rem;
  }
  
  .profile-section h3 {
    color: #4b5563;
    margin-bottom: 1rem;
  }
  
  .info-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
  }
  
  .info-item label {
    font-size: 0.875rem;
    color: #6b7280;
    display: block;
    margin-bottom: 0.5rem;
  }
  
  .info-item p, .info-item a {
    color: #111827;
    margin: 0;
  }
  
  .description {
    line-height: 1.6;
    color: #374151;
  }
  
  .profile-actions {
    margin-top: 2rem;
    display: flex;
    justify-content: flex-end;
  }
  
  .edit-button {
    background: #5d6c8d;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 0.375rem;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }
  
  .edit-button:hover {
    background: #4a5578;
  }
</style>