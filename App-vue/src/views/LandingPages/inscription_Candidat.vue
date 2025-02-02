<script setup>
import { ref, reactive, onMounted, onUnmounted } from "vue";
import { registerStudent } from '@/apiClient';
import { useRouter } from 'vue-router';
import DefaultNavbar from "./navbars/NavbarDefaults.vue";
import DefaultFooter from "./footers/FooterDefault.vue";

const router = useRouter();
const isLoading = ref(false);

const formData = reactive({
  prenom: "",         
  nom: "",            
  numero_telephone: "", 
  etablissement: "",   
  filiere: "",        
  niveau_etude: "",   
  annee_graduation: "",
  type_recherche: "", 
  date_disponibilite: "",
  photo: null,
  cv: null,
  portfolio: null,
  username: "",
  email: "",
  password: ""
});

const errors = reactive({
  prenom: "",
  nom: "",
  numero_telephone: "",
  etablissement: "",
  filiere: "",
  niveau_etude: "",
  annee_graduation: "",
  type_recherche: "",
  date_disponibilite: "",
  photo: "",
  cv: "",
  portfolio: "",
  username: "",
  email: "",
  password: ""
});

const clearErrors = () => {
  Object.keys(errors).forEach(key => {
    errors[key] = "";
  });
};

const validateForm = () => {
  let isValid = true;
  clearErrors();

  const requiredFields = [
    'prenom', 'nom', 'numero_telephone', 'etablissement', 
    'filiere', 'niveau_etude', 'annee_graduation', 
    'type_recherche', 'date_disponibilite', 'username', 
    'email', 'password'
  ];

  requiredFields.forEach(field => {
    if (!formData[field]) {
      errors[field] = 'Ce champ est requis';
      isValid = false;
    }
  });

  // Validation de l'username (pas d'espaces)
  if (formData.username && formData.username.includes(' ')) {
    errors.username = "Le nom d'utilisateur ne doit pas contenir d'espaces";
    isValid = false;
  }

  // Validation du format de la date (YYYY-MM-DD)
  if (formData.date_disponibilite) {
    const dateRegex = /^\d{4}-\d{2}-\d{2}$/;
    if (!dateRegex.test(formData.date_disponibilite)) {
      errors.date_disponibilite = 'La date doit être au format YYYY-MM-DD';
      isValid = false;
    }
  }

  // Validation email
  if (formData.email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
    errors.email = 'Adresse email invalide';
    isValid = false;
  }

  // Validation mot de passe
  if (formData.password && formData.password.length < 8) {
    errors.password = 'Le mot de passe doit contenir au moins 8 caractères';
    isValid = false;
  }

  // Validation année de graduation
  const year = parseInt(formData.annee_graduation);
  if (isNaN(year) || year < new Date().getFullYear() || year > new Date().getFullYear() + 10) {
    errors.annee_graduation = 'Année de graduation invalide';
    isValid = false;
  }

  return isValid;
};

const handleFormSubmit = async (e) => {
  e.preventDefault();
  console.log("Début de la soumission du formulaire");
  
  if (!validateForm()) {
    console.log("Échec de la validation du formulaire");
    alert("Veuillez corriger les erreurs dans le formulaire");
    return;
  }

  isLoading.value = true;
  console.log("Données du formulaire avant envoi:", formData);

  try {
    const formDataToSend = new FormData();
    
    // Mappage des champs
    const mapping = {
      'firstName': formData.prenom,
      'lastName': formData.nom,
      'phoneNumber': formData.numero_telephone,
      'institution': formData.etablissement,
      'fieldOfStudy': formData.filiere,
      'educationLevel': formData.niveau_etude,
      'graduationYear': formData.annee_graduation,
      'researchType': formData.type_recherche,
      'availabilityDate': formData.date_disponibilite,
      'username': formData.username,
      'email': formData.email,
      'password': formData.password
    };

    // Ajout des champs au FormData avec log
    Object.entries(mapping).forEach(([key, value]) => {
      if (value) {
        formDataToSend.append(key, value);
        console.log(`Ajout au FormData: ${key}:`, value);
      }
    });

    // Ajout des fichiers
    if (formData.photo instanceof File) {
      formDataToSend.append('photo', formData.photo);
      console.log('Ajout de la photo:', formData.photo.name);
    }
    if (formData.cv instanceof File) {
      formDataToSend.append('cv', formData.cv);
      console.log('Ajout du CV:', formData.cv.name);
    }
    if (formData.portfolio instanceof File) {
      formDataToSend.append('portfolio', formData.portfolio);
      console.log('Ajout du portfolio:', formData.portfolio.name);
    }

    console.log("Envoi de la requête...");
    const response = await registerStudent(formDataToSend);
    console.log("Réponse reçue:", response);
    
    if (response && response.message === 'Registration successful') {
      alert("Inscription réussie !");
      router.push('/login');
    }
  } catch (error) {
    console.error("Erreur lors de l'inscription:", error);
    if (error.response) {
      console.error("Détails de l'erreur:", error.response.data);
      // Afficher les erreurs spécifiques si disponibles
      if (typeof error.response.data === 'object') {
        Object.entries(error.response.data).forEach(([field, message]) => {
          errors[field] = Array.isArray(message) ? message[0] : message;
        });
      }
    }
    alert("Une erreur est survenue lors de l'inscription. Veuillez vérifier les champs et réessayer.");
  } finally {
    isLoading.value = false;
  }
};

const handleFileUpload = (event, key) => {
  const file = event.target.files[0];
  if (file) {
    const maxSize = 5 * 1024 * 1024; // 5MB
    if (file.size > maxSize) {
      errors[key] = 'Le fichier est trop volumineux (max 5MB)';
      event.target.value = ''; // Reset input
      return;
    }
    formData[key] = file;
    errors[key] = ''; // Clear any previous error
  }
};

onMounted(() => {
  document.body.classList.add("about-us", "bg-light");
});

onUnmounted(() => {
  document.body.classList.remove("about-us", "bg-light");
});
</script>


<template>
  <!-- Loading Overlay -->
  <div v-if="isLoading" class="loading-overlay">
    <div class="loading-spinner"></div>
  </div>

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
      <section class="py-6"></section>
      <div class="header-center">
        <a href="#">
          <img
            src="@/assets/img/logo-removebg-preview.png"
            style="width: 150px;"
            class="img-fluid"
            alt="Logo"
          />
        </a>
        <section class="py-2"></section>
        <h3>Formulaire d'Inscription Candidat</h3>
        <h6>Veuillez remplir le formulaire ci-dessous</h6>
      </div>

      <section class="py-4"></section>
      <form @submit.prevent="handleFormSubmit">
        <div class="form-sections">
          <div class="form-section-left">
            <div class="form-group">
              <h4>Informations Personnelles</h4>
            </div>
            <!-- Champs personnels -->
            <div class="form-group">
              <label>Prénom</label>
              <input 
                type="text" 
                class="text-btn" 
                v-model="formData.prenom" 
                :class="{ 'error-input': errors.prenom }"
                placeholder="Entrez votre prénom" 
              />
              <span v-if="errors.prenom" class="error">{{ errors.prenom }}</span>
            </div>
            <div class="form-group">
              <label>Nom</label>
              <input type="text" class="text-btn" v-model="formData.nom" placeholder="Entrez votre nom" />
              <span v-if="errors.nom" class="error">{{ errors.nom }}</span>
            </div>
            <div class="form-group">
              <label>Numéro de téléphone</label>
              <input type="text" class="text-btn" v-model="formData.numero_telephone" placeholder="Entrez votre numéro de téléphone" />
              <span v-if="errors.numero_telephone" class="error">{{ errors.numero_telephone }}</span>
            </div>
            <div class="form-group">
              <label>Nom d'utilisateur</label>
              <input type="text" class="text-btn" v-model="formData.username" placeholder="Entrez votre nom d'utilisateur" />
              <span v-if="errors.username" class="error">{{ errors.username }}</span>
            </div>
            <div class="form-group">
              <label>Photo de profil</label>
              <input type="file" class="custom-file-input" @change="(e) => handleFileUpload(e, 'photo')" accept="image/*" />
              <span v-if="errors.photo" class="error">{{ errors.photo }}</span>
            </div>
            <div class="form-group">
              <label>CV</label>
              <input type="file" class="custom-file-input" @change="(e) => handleFileUpload(e, 'cv')" accept=".pdf, .doc, .docx" />
              <span v-if="errors.cv" class="error">{{ errors.cv }}</span>
            </div>
            <div class="form-group">
              <label>Portfolio</label>
              <input type="file" class="custom-file-input" @change="(e) => handleFileUpload(e, 'portfolio')" accept=".pdf, .doc, .docx" />
            </div>
          </div>

          <!-- Section droite avec les informations sur l'éducation -->
<div class="form-section-right">
  <div class="form-group">
    <h4>Informations sur l'Éducation</h4>
  </div>
  <div class="form-group">
    <label>Établissement</label>
    <input 
      type="text" 
      class="text-btn" 
      v-model="formData.etablissement" 
      :class="{ 'error-input': errors.etablissement }"
      placeholder="Entrez votre établissement" 
    />
    <span v-if="errors.etablissement" class="error">{{ errors.etablissement }}</span>
  </div>
  <div class="form-group">
    <label>Filière</label>
    <input 
      type="text" 
      class="text-btn" 
      v-model="formData.filiere" 
      :class="{ 'error-input': errors.filiere }"
      placeholder="Entrez votre filière" 
    />
    <span v-if="errors.filiere" class="error">{{ errors.filiere }}</span>
  </div>
  <div class="form-group">
    <label>Niveau d'étude</label>
    <input 
      type="text" 
      class="text-btn" 
      v-model="formData.niveau_etude" 
      :class="{ 'error-input': errors.niveau_etude }"
      placeholder="Entrez votre niveau d'étude" 
    />
    <span v-if="errors.niveau_etude" class="error">{{ errors.niveau_etude }}</span>
  </div>
  <div class="form-group">
    <label>Année de graduation</label>
    <input 
      type="text" 
      class="text-btn" 
      v-model="formData.annee_graduation" 
      :class="{ 'error-input': errors.annee_graduation }"
      placeholder="Entrez votre année de graduation" 
    />
    <span v-if="errors.annee_graduation" class="error">{{ errors.annee_graduation }}</span>
  </div>
  <div class="form-group">
    <label>Type de recherche</label>
    <input 
      type="text" 
      class="text-btn" 
      v-model="formData.type_recherche" 
      :class="{ 'error-input': errors.type_recherche }"
      placeholder="Entrez votre type de recherche" 
    />
    <span v-if="errors.type_recherche" class="error">{{ errors.type_recherche }}</span>
  </div>
  <div class="form-group">
    <label>Date de disponibilité</label>
    <input 
      type="text" 
      class="text-btn" 
      v-model="formData.date_disponibilite" 
      :class="{ 'error-input': errors.date_disponibilite }"
      placeholder="YYYY-MM-DD" 
    />
    <span v-if="errors.date_disponibilite" class="error">{{ errors.date_disponibilite }}</span>
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
              <input type="email" class="text-btn" v-model="formData.email" placeholder="Entrez votre email" />
              <span v-if="errors.email" class="error">{{ errors.email }}</span>
            </div>

            <div class="form-group">
              <label>Mot de passe</label>
              <input type="password" class="text-btn" v-model="formData.password" placeholder="Entrez votre mot de passe" />
              <span v-if="errors.password" class="error">{{ errors.password }}</span>
            </div>
        </div>
        <section class="py-2"></section>
        <button 
          type="submit" 
          class="submit-button"
          :disabled="isLoading"
        >
          {{ isLoading ? 'Inscription en cours...' : 'Soumettre' }}
        </button>
      </form>
      <section class="py-3"></section>
      <p class="footer-text">
        Vous avez déjà un compte ? <a href="/login">Se connecter</a>
      </p>
    </div>
  </div>
  <section class="py-7"></section>
  <DefaultFooter />
</template>

<style scoped>
  .login-page {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 220vh;
  }

  .login-container {
    width: 100%;
    max-width: 3000px;
    background: #fff;
    padding: 100px;
    border-radius: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    text-align: center;
  }

  .header-center {
    margin-bottom: 10px;
  }

  .header-center img {
    width: 170px;
  }

  .header-center h2 {
    margin-top: 10px;
  }

  .form-group input, .form-group textarea {
    width: 100%;
    padding: 20px;
    margin-top: 10px;
    border: 1px solid #ccc;
    border-radius: 12px;
  }
  .form-section-center{
    flex-direction: column;  
    justify-content: center;
    width: 50%; /* Ajustez si nécessaire */
    max-width: 650px; /* Limitez la largeur si souhaité */
    margin: 0 auto; /* Centre horizontalement */
    padding: 20px; /* Espace interne */
    box-sizing: border-box;
  }

  .form-sections {
    display: flex;
    justify-content: space-between;
  }

  .form-section-left{
    width: 45%;
  }

  .form-section-right {
    width: 45%;
  }

  .form-group {
    margin-bottom: 20px;
    text-align: left;
  }

  .form-group input {
    width: 100%;
    padding: 9px;
    margin-top: 2px;
    border: 1px solid #ccc;
    border-radius: 10px;
  }

  .error {
    color: red;
    font-size: 12px;
    margin-top: 5px;
  }

  .submit-button {
    width: 100%;
    padding: 9px;
    background: #5d6c8d;
    color: #fff;
    border: none;
    border-radius: 10px;
    cursor: pointer;
  }

  .footer-text {
    margin-top: 0px;
    color: #666;
  }

  .footer-text a {
    color: #5d6c8d;
    text-decoration: none;
  }
  .form-group-inline {
  display: flex;
  justify-content: space-between;
  gap: 30px; /* Espace entre les deux champs */
}

.form-group-inline .form-group {
  flex: 1;
}

.custom-file-input {
  position: relative;
  display: inline-block;
  width: auto;
}

.custom-file-input::before {
  content: "Choisir un fichier";
  display: inline-block;
  background-color: #5d6c8d;
  color: white;
  border: none;
  padding: 5px 30px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 14px;
  font-family: Arial, sans-serif;
  transition: background-color 0.3s ease;
}

.custom-file-input:hover::before {
  background-color: #42668b;
}

.custom-file-input:active::before {
  background-color: #4c79a7;
}

.custom-file-input::-webkit-file-upload-button {
  visibility: hidden; /* Masque le bouton natif */
}

.text-btn{
    font-size: 14px;
  }

label {
  font-size: 16px; /* Taille de l'écriture */
  display: block;
  margin-bottom: 5px;
}
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(255, 255, 255, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

.loading-spinner {
  width: 50px;
  height: 50px;
  border: 5px solid #f3f3f3;
  border-top: 5px solid #5d6c8d;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.error-input {
  border-color: #ff4444 !important;
}

.submit-button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

</style>
