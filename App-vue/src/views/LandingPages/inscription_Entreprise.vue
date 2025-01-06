<script setup>
import { ref, reactive, onMounted, onUnmounted } from "vue";

// Import des composants
import DefaultNavbar from "./navbars/NavbarDefaults.vue";
import DefaultFooter from "./footers/FooterDefault.vue";

// États pour gérer les données du formulaire
const formData = reactive({
  companyName: "",
  companyLogo: null,
  sector: "",
  description: "",
  website: "",
  phoneNumber: "",
  address: "",
  companySize: "",
  creationYear: "",
  username: "",
  email: "",
  password: "",
});

const errors = reactive({});

// Fonction de soumission du formulaire
const handleFormSubmit = () => {
  // Réinitialisation des erreurs
  Object.keys(errors).forEach((key) => {
    errors[key] = "";
  });

  // Validation des champs
  if (!formData.companyName) errors.companyName = "Le nom de la société est requis.";
  if (!formData.sector) errors.sector = "Le secteur d'activité est requis.";
  if (!formData.website) errors.website = "Le site web est requis.";
  if (!formData.phoneNumber) errors.phoneNumber = "Le numéro de téléphone est requis.";
  if (!formData.address) errors.address = "L'adresse est requise.";
  if (!formData.companySize) errors.companySize = "La taille de l'entreprise est requise.";
  if (!formData.creationYear) errors.creationYear = "L'année de création est requise.";
  if (!formData.username) errors.username = "Le nom d'utilisateur est requis.";
  if (!formData.email) {
    errors.email = "L'email est requis.";
  } else if (!/\S+@\S+\.\S+/.test(formData.email)) {
    errors.email = "Format de l'email invalide.";
  }
  if (!formData.password) errors.password = "Le mot de passe est requis.";

  if (Object.values(errors).every((error) => !error)) {
    alert("Formulaire soumis avec succès !");
    // Logique pour soumettre les données
  }
};

// Gestion des fichiers téléchargés
const handleFileUpload = (event, key) => {
  const file = event.target.files[0];
  if (file) {
    formData[key] = file;
  }
};

// Hooks pour gérer la classe du body
const body = document.getElementsByTagName("body")[0];
onMounted(() => {
  body.classList.add("about-us");
  body.classList.add("bg-light");

  if (document.getElementById("typed")) {
    new Typed("#typed", {
      stringsElement: "#typed-strings",
      typeSpeed: 90,
      backSpeed: 90,
      backDelay: 200,
      startDelay: 500,
      loop: true,
    });
  }
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
      <section class="py-6"></section>
      <div class="header-center">
        <a href="#">
          <img
            src="@/assets/img/logo-removebg-preview.png"
            style="width: 150px;"
            class="img-fluid"
          />
        </a>
        <section class="py-2"></section>
        <h3>Formulaire d'Inscription Société</h3>
        <h6>Veuillez remplir le formulaire ci-dessous</h6>
      </div>

      <section class="py-4"></section>
      <form @submit.prevent="handleFormSubmit">
        <!-- Division en deux parties : gauche et droite -->
        <div class="form-sections">
          <div class="form-section-left">
            <div class="form-group">
              <h4>Informations de la Société</h4>
            </div>
            <div class="form-group">
              <label>Nom de la société</label>
              <input type="text" class="text-btn" v-model="formData.companyName" placeholder="Entrez le nom de la société" />
              <span v-if="errors.companyName" class="error">{{ errors.companyName }}</span>
            </div>

            <div class="form-group">
              <label>Secteur d'activité</label>
              <input type="text" class="text-btn" v-model="formData.sector" placeholder="Entrez le secteur d'activité" />
              <span v-if="errors.sector" class="error">{{ errors.sector }}</span>
            </div>

            <div class="form-group">
              <label>Site Web</label>
              <input type="text" class="text-btn" v-model="formData.website" placeholder="Entrez l'URL du site web" />
              <span v-if="errors.website" class="error">{{ errors.website }}</span>
            </div>

            <div class="form-group">
              <label>Numéro de téléphone</label>
              <input type="text" class="text-btn" v-model="formData.phoneNumber" placeholder="Entrez le numéro de téléphone" />
              <span v-if="errors.phoneNumber" class="error">{{ errors.phoneNumber }}</span>
            </div>

            <div class="form-group">
              <label>Adresse</label>
              <input type="text" class="text-btn" v-model="formData.address" placeholder="Entrez l'adresse de la société" />
              <span v-if="errors.address" class="error">{{ errors.address }}</span>
            </div>

          </div>

          <div class="form-section-right">
            <section class="py-4"></section>
            <section class="py-1"></section>
            <div class="form-group">
              <label>Description</label>
              <textarea class="text-btn" v-model="formData.description" placeholder="Entrez une brève description de la société"></textarea>
            </div>

            <div class="form-group">
              <label>Taille de l'entreprise</label>
              <input type="text" class="text-btn" v-model="formData.companySize" placeholder="Entrez la taille de l'entreprise" />
              <span v-if="errors.companySize" class="error">{{ errors.companySize }}</span>
            </div>

            <div class="form-group">
              <label>Année de création</label>
              <input type="text" class="text-btn" v-model="formData.creationYear" placeholder="Entrez l'année de création de la société" />
              <span v-if="errors.creationYear" class="error">{{ errors.creationYear }}</span>
            </div>

            <div class="form-group">
              <label>Logo de la société</label>
              <input type="file" class="custom-file-input" @change="(e) => handleFileUpload(e, 'companyLogo')" accept="image/*" />
            </div>
            

          </div>
        </div>

        <section class="py-3"></section>
        <div class="form-section-center">
            <div class="form-group">
                  <h4>Identification</h4>
            </div>
            <div class="form-group">
              <label>Nom d'utilisateur</label>
              <input type="text" class="text-btn" v-model="formData.username" placeholder="Nom d'utilisateur" />
              <span v-if="errors.username" class="error">{{ errors.username }}</span>
            </div>

            <div class="form-group">
              <label>Email</label>
              <input type="email" class="text-btn" v-model="formData.email" placeholder="Entrez l'email" />
              <span v-if="errors.email" class="error">{{ errors.email }}</span>
            </div>

            <div class="form-group">
              <label>Mot de passe</label>
              <input type="password" class="text-btn" v-model="formData.password" placeholder="Entrez le mot de passe" />
              <span v-if="errors.password" class="error">{{ errors.password }}</span>
            </div>
          </div>
          <section class="py-2"></section>
        <button type="submit" class="submit-button">Soumettre</button>
      </form>

      <section class="py-3"></section>
      <p class="footer-text">
        Vous avez déjà un compte ? <a href="/login">Se connecter</a>
      </p>
    </div>
  </div>
  <section class="py-6"></section>
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

</style>
