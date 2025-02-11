<script setup>
import { ref, reactive, onMounted, onUnmounted } from "vue";
import { registerCompany } from '@/apiClient';
import { useRouter } from 'vue-router';
import DefaultNavbar from "./navbars/NavbarDefaults.vue";
import DefaultFooter from "./footers/FooterDefault.vue";

const router = useRouter();
const isLoading = ref(false);

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
  password: ""
});

const errors = reactive({});

const validateForm = () => {
  let isValid = true;
  Object.keys(errors).forEach(key => {
    errors[key] = "";
  });

  // Validation des champs requis
  const requiredFields = [
    'companyName', 'sector', 'website', 'phoneNumber', 
    'address', 'companySize', 'creationYear', 'username', 
    'email', 'password'
  ];

  requiredFields.forEach(field => {
    if (!formData[field]) {
      errors[field] = 'Ce champ est requis';
      isValid = false;
    }
  });

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

  return isValid;
};

const handleFormSubmit = async (e) => {
  e.preventDefault();
  
  if (!validateForm()) {
    alert("Veuillez corriger les erreurs dans le formulaire");
    return;
  }

  isLoading.value = true;

  try {
    const formDataToSend = new FormData();
    
    // Ajout des champs au FormData
    Object.entries(formData).forEach(([key, value]) => {
      if (value && key !== 'companyLogo') {
        formDataToSend.append(key, value);
      }
    });

    // Ajout du logo s'il existe
    if (formData.companyLogo instanceof File) {
      formDataToSend.append('companyLogo', formData.companyLogo);
    }

    const response = await registerCompany(formDataToSend);
    
    if (response && response.message === 'Registration successful') {
      alert("Inscription réussie !");
      router.push('/login');
    }
  } catch (error) {
    console.error("Erreur lors de l'inscription:", error);
    if (error.response) {
      Object.entries(error.response.data).forEach(([field, message]) => {
        errors[field] = Array.isArray(message) ? message[0] : message;
      });
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
      event.target.value = '';
      return;
    }
    formData[key] = file;
    errors[key] = '';
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
