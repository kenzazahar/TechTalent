<template>
  <header class="bg-gradient-white">
    <div class="page-header min-vh-60">
      <span class="mask bg-gradient-white opacity-6"></span>
      <div class="container">
        <DefaultNavbar />
      </div>
    </div>
  </header>
  <section class="py-5"></section>
  <div class="login-page">
    <div class="login-container">
      <div style="text-align: center;">
        <a href="#">
          <img
            src="@/assets/img/logo-removebg-preview.png"
            style="width: 170px;"
            class="img-fluid"
          />
        </a>
      </div>
      <section class="py-3"></section>
      <h3>Bienvenue, nous sommes ravis de vous retrouver</h3>
      <p>Veuillez entrer vos identifiants pour continuer</p>

      <form @submit.prevent="handleLogin">
        <div class="form-group">
          <label>Adresse e-mail / Nom d'utilisateur</label>
          <input type="text" v-model="email" placeholder="Entrez votre e-mail" />
          <span v-if="errors.email" class="error">{{ errors.email }}</span>
        </div>

        <div class="form-group">
          <label>Mot de passe</label>
          <input
            type="password"
            v-model="password"
            placeholder="Entrez votre mot de passe"
          />
          <span v-if="errors.password" class="error">{{ errors.password }}</span>
        </div>

        <div class="form-options">
          <label>
            <input type="checkbox" v-model="rememberMe" /> Se souvenir de moi ?
          </label>
          <a href="#" class="forgot-password">Mot de passe oublié ?</a>
        </div>

        <button type="submit" class="login-button">Se connecter</button>
      </form>

      <p class="footer-text">
        Vous n'avez pas de compte ? 
        <RouterLink to="/connexion">S'inscrire</RouterLink>
      </p>
    </div>
  </div>
  <section class="py-4"></section>
  <DefaultFooter />
</template>

<script setup>
import { ref, reactive, onMounted, onUnmounted } from "vue";
import Typed from "typed.js";

// example components
import DefaultNavbar from "./navbars/NavbarDefaults.vue";
import DefaultFooter from "./footers/FooterDefault.vue";

// State
const email = ref("");
const password = ref("");
const rememberMe = ref(false);
const errors = reactive({});

const handleLogin = () => {
  // Reset errors
  errors.email = "";
  errors.password = "";

  if (!email.value) {
    errors.email = "L'email est requis.";
  } else if (!/\S+@\S+\.\S+/.test(email.value)) {
    errors.email = "Format de l'email invalide.";
  }

  if (!password.value) {
    errors.password = "Le mot de passe est requis.";
  } else if (password.value.length < 6) {
    errors.password = "Le mot de passe doit contenir au moins 6 caractères.";
  }

  if (!errors.email && !errors.password) {
    alert("Login successful!");
    // Add login logic here
  }
};

// On mounted and unmounted hooks
const body = document.getElementsByTagName("body")[0];
onMounted(() => {
  body.classList.add("about-us");
  body.classList.add("bg-white");

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

<style scoped>
  .login-page {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 90vh;
  }
  
  .login-container {
    width: 600px;
    background: #fff;
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    text-align: center;
  }
  
  .divider {
    margin: 20px 0;
    color: #b6b6ba;
  }
  
  .form-group {
    margin-bottom: 20px;
    text-align: left;
  }
  
  .form-group input {
    width: 100%;
    padding: 13px;
    margin-top: 5px;
    border: 1px solid #ccc;
    border-radius: 12px;
  }
  
  .error {
    color: red;
    font-size: 12px;
  }
  
  .form-options {
    display: flex;
    justify-content: space-between;
    margin: 20px 0;
  }
  
  .forgot-password {
    color: #5d6c8d;
    text-decoration: none;
  }
  
  .login-button {
    width: 100%;
    padding: 12px;
    background: #5d6c8d;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .footer-text {
    margin-top: 15px;
    color: #666;
  }
  
  .footer-text a {
    color: #5d6c8d;
    text-decoration: none;
  }
  .bg-gray {
    background-color: #1f4266; /* Exemple de gris clair */
  }
</style>
