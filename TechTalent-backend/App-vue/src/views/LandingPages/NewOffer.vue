<script setup>
import { ref, reactive, onMounted, onUnmounted } from "vue";
import { useRouter } from "vue-router";
import { useJobOffersStore } from '@/stores/jobOffersStore.js';
import DefaultFooter from "./footers/FooterDefault.vue";

const router = useRouter();
const jobOffersStore = useJobOffersStore();
const isSubmitting = ref(false);

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

const validateForm = (isPublish) => {
  Object.keys(errors).forEach((key) => {
    errors[key] = "";
  });

  if (!formData.title) {
    errors.title = "Le titre est requis.";
    return false;
  }

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

const saveAsDraft = async () => {
  if (!validateForm(false)) {
    return;
  }

  try {
    isSubmitting.value = true;
    await jobOffersStore.createOffer(formData, false);
    alert("Offre sauvegardée comme brouillon !");
    router.push("/dashboard");
  } catch (error) {
    alert("Erreur lors de la sauvegarde: " + error.message);
  } finally {
    isSubmitting.value = false;
  }
};

const publishOffer = async () => {
  console.log("Tentative de publication...");
  if (!validateForm(true)) {
    console.log("Validation échouée", errors);
    return;
  }

  try {
    isSubmitting.value = true;
    console.log("FormData envoyé :", formData);

    const response = await jobOffersStore.createOffer(formData, true); // Assurez-vous que isPublish est true
    console.log("Réponse de l'API :", response);

    alert("Offre publiée avec succès !");
    router.push("/dashboard");
  } catch (error) {
    console.error("Erreur lors de la publication:", error);
    alert("Erreur lors de la publication: " + (error.message || "Réponse vide"));
  } finally {
    isSubmitting.value = false;
  }
};




const body = document.getElementsByTagName("body")[0];
onMounted(() => {
  body.classList.add("about-us");
  body.classList.add("bg-light");
});

onUnmounted(() => {
  body.classList.remove("about-us");
  body.classList.remove("bg-light");
});
</script>

<template>
  <header class="bg-gradient-white">
    <div class="page-header min-vh-60">
      <span class="mask bg-gradient-white opacity-6"></span>
      <div class="container">
        <DefaultNavbar style="background-color: white;" />
      </div>
    </div>
  </header>

  <div class="login-page">
    <div class="login-container">
      <h3>Nouvelle offre</h3>
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
            <button type="button" class="cancel-button" @click="cancelAction">Annuler</button>
          <button type="button" class="draft-button" @click="saveAsDraft">Sauvegarder comme brouillon</button>
          <button type="submit" class="submit-button">Publier</button>
        </div>
      </form>
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
    background: #767474;
    color: #fff;
  }
  .cancel-button:hover {
  background-color: #474343;
}

  .draft-button {
    background: #343435;
    color: #fff;
  }
  .draft-button:hover {
  background-color: #1f1d1d;
}
  .submit-button {
    background: #0d0a1a;
    color: #fff;
  }
  .submit-button:hover {
  background-color: #060505;
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
