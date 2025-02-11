<template>
  <div class="edit-profile-page">
    <div v-if="loading" class="loading-overlay">
      <div class="loading-spinner">Chargement...</div>
    </div>
    <div class="edit-container">
      <section class="py-4"></section>
      <div class="header-center">
        <h3>Modifier mon Profil</h3>
        <h6>Modifier vos informations personnelles</h6>
      </div>

      <section class="py-4"></section>
      <form @submit.prevent="confirmSave">
        <div class="form-sections">
          <div class="form-section-left">
            <div class="form-group">
              <h4>Informations Personnelles</h4>
            </div>
            <div class="form-group-inline">
              <div class="form-group">
                <label>Prénom</label>
                <input type="text" class="text-btn" v-model="formData.firstName" />
                <span v-if="errors.firstName" class="error">{{ errors.firstName }}</span>
              </div>
              <div class="form-group">
                <label>Nom</label>
                <input type="text" class="text-btn" v-model="formData.lastName" />
                <span v-if="errors.lastName" class="error">{{ errors.lastName }}</span>
              </div>
            </div>

            <div class="form-group">
              <label>Numéro de téléphone</label>
              <input type="text" class="text-btn" v-model="formData.phoneNumber" />
              <span v-if="errors.phoneNumber" class="error">{{ errors.phoneNumber }}</span>
            </div>

            <div class="form-group">
              <label>Nom d'utilisateur</label>
              <input type="text" class="text-btn" v-model="formData.username" />
              <span v-if="errors.username" class="error">{{ errors.username }}</span>
            </div>

            <div class="form-group">
              <label>Photo de profil</label>
              <div class="photo-preview" v-if="formData.photo">
                <img :src="formData.photo" alt="Photo actuelle" />
              </div>
              <input type="file" id="profile-photo" class="custom-file-input" @change="handleFileUpload($event, 'photo')" accept="image/*" />
              <label for="profile-photo">Choisir une photo</label>
            </div>

            <div class="form-group">
              <label>CV</label>
              <input type="file" id="cv-file" class="custom-file-input" @change="handleFileUpload($event, 'cv')" accept=".pdf,.doc,.docx" />
              <label for="cv-file">Choisir un CV</label>
            </div>

            <div class="form-group">
              <label>Portfolio</label>
              <input type="file" id="portfolio-file" class="custom-file-input" @change="handleFileUpload($event, 'portfolio')" accept=".pdf,.doc,.docx" />
              <label for="portfolio-file">Choisir un portfolio</label>
            </div>
          </div>

          <div class="form-section-right">
            <div class="form-group">
              <h4>Informations sur l'Éducation</h4>
            </div>

            <div class="form-group">
              <label>Établissement</label>
              <input type="text" class="text-btn" v-model="formData.institution" />
              <span v-if="errors.institution" class="error">{{ errors.institution }}</span>
            </div>

            <div class="form-group">
              <label>Filière</label>
              <input type="text" class="text-btn" v-model="formData.fieldOfStudy" />
              <span v-if="errors.fieldOfStudy" class="error">{{ errors.fieldOfStudy }}</span>
            </div>

            <div class="form-group">
              <label>Niveau d'étude</label>
              <input type="text" class="text-btn" v-model="formData.educationLevel" />
              <span v-if="errors.educationLevel" class="error">{{ errors.educationLevel }}</span>
            </div>

            <div class="form-group">
              <label>Année de graduation</label>
              <input type="text" class="text-btn" v-model="formData.graduationYear" />
              <span v-if="errors.graduationYear" class="error">{{ errors.graduationYear }}</span>
            </div>

            <div class="form-group">
              <label>Type de recherche</label>
              <input type="text" class="text-btn" v-model="formData.researchType" />
              <span v-if="errors.researchType" class="error">{{ errors.researchType }}</span>
            </div>

            <div class="form-group">
              <label>Date de disponibilité</label>
              <input type="text" class="text-btn" v-model="formData.availabilityDate" />
              <span v-if="errors.availabilityDate" class="error">{{ errors.availabilityDate }}</span>
            </div>
          </div>
        </div>

        <section class="py-3"></section>
        <div class="form-section-center">
          <div class="form-group">
            <h4>Identification</h4>
          </div>
          <div class="form-group">
            <label>Email</label>
            <input type="email" class="text-btn" v-model="formData.email" />
            <span v-if="errors.email" class="error">{{ errors.email }}</span>
          </div>
        </div>

        <div class="buttons-container">
          <button type="button" @click="handleCancel" class="cancel-button">Annuler</button>
          <button type="submit" class="save-button">Sauvegarder</button>
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
import { useRouter } from "vue-router";
import DefaultFooter from "./footers/FooterDefault.vue";
import { getProfile, updateProfile } from "@/apiClient";

const router = useRouter();
const showConfirmModal = ref(false);
const loading = ref(false);

const formData = reactive({
  firstName: "",
  lastName: "",
  phoneNumber: "",
  photo: null,
  institution: "",
  fieldOfStudy: "",
  educationLevel: "",
  graduationYear: "",
  researchType: "",
  availabilityDate: "",
  cv: null,
  portfolio: null,
  username: "",
  email: "",
});

const errors = reactive({});

// Charger les données du profil
onMounted(async () => {
  try {
    loading.value = true;
    const profileData = await getProfile();
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
  router.push("/candidate/dashboard");
};

const validateForm = () => {
  const newErrors = {};
  if (!formData.firstName) newErrors.firstName = "Le prénom est requis";
  if (!formData.lastName) newErrors.lastName = "Le nom est requis";
  if (!formData.email) newErrors.email = "L'email est requis";
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
    await updateProfile(form);
    router.push("/candidate/dashboard");
  } catch (error) {
    console.error("Erreur lors de la sauvegarde:", error);
  } finally {
    loading.value = false;
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

.form-group-inline {
  display: flex;
  gap: 1rem;
}

.form-group-inline .form-group {
  flex: 1;
}

.photo-preview {
  margin-bottom: 1rem;
}

.photo-preview img {
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

.form-section-center {
  width: 50%;
  margin: 0 auto;
}

.error {
  color: #dc2626;
  font-size: 0.75rem;
  margin-top: 0.25rem;
}
</style>