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
            style="width: 130px;"
            class="img-fluid"
          />
        </a>
      </div>
      <section class="py-2"></section>
      <h5>Bienvenue, nous sommes ravis de vous retrouver</h5>
      <p>Veuillez entrer vos identifiants pour continuer</p>

      <section class="py-2"></section>
      <form @submit.prevent="handleLogin">
        <div class="form-group">
          <label>Nom d'utilisateur</label>
          <input 
            type="text" 
            v-model="username" 
            placeholder="Entrez votre nom d'utilisateur"  
            class="text-btn"
            :class="{ 'error-input': errors.username }"
          />
          <span v-if="errors.username" class="error">{{ errors.username }}</span>
        </div>

        <div class="form-group">
          <label>Mot de passe</label>
          <input
            type="password"
            v-model="password"
            placeholder="Entrez votre mot de passe"
            class="text-btn"
            :class="{ 'error-input': errors.password }"
          />
          <span v-if="errors.password" class="error">{{ errors.password }}</span>
        </div>

        <div class="form-options">
          <label>
            <input type="checkbox" v-model="rememberMe" /> Se souvenir de moi ?
          </label>
          <a href="#" class="forgot-password forget-text">Mot de passe oublié ?</a>
        </div>

        <button 
          type="submit" 
          class="login-button"
          :disabled="isLoading"
        >
          {{ isLoading ? 'Connexion en cours...' : 'Se connecter' }}
        </button>
        
        <div v-if="apiError" class="error-message">
          {{ apiError }}
        </div>
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
import { useRouter } from 'vue-router';
import { loginUser } from '@/apiClient';
import Typed from "typed.js";
import DefaultNavbar from "./navbars/NavbarDefaults.vue";
import DefaultFooter from "./footers/FooterDefault.vue";

const router = useRouter();
const username = ref("");
const password = ref("");
const rememberMe = ref(false);
const isLoading = ref(false);
const apiError = ref("");
const errors = reactive({
  username: "",
  password: ""
});

const validateForm = () => {
  let isValid = true;
  errors.username = "";
  errors.password = "";
  apiError.value = "";

  if (!username.value) {
    errors.username = "Le nom d'utilisateur est requis";
    isValid = false;
  }

  if (!password.value) {
    errors.password = "Le mot de passe est requis";
    isValid = false;
  } else if (password.value.length < 6) {
    errors.password = "Le mot de passe doit contenir au moins 6 caractères";
    isValid = false;
  }

  return isValid;
};

const handleLogin = async () => {
  if (!validateForm()) {
    return;
  }

  isLoading.value = true;
  apiError.value = "";

  try {
    const response = await loginUser({
      username: username.value,
      password: password.value,
    });

    if (response.message === 'Login successful') {
      // Store authentication details
      localStorage.setItem('isAuthenticated', 'true');
      localStorage.setItem('username', response.username);
      localStorage.setItem('userType', response.user_type);
      
      if (rememberMe.value) {
        localStorage.setItem('userEmail', username.value);
      }

      // Redirection basée sur le type d'utilisateur
      if (response.user_type === 'student') {
        router.push('/candidate/dashboard');
      } else if (response.user_type === 'company') {
        router.push('/dashboard');
      }
    }
  } catch (error) {
    console.error('Login error:', error);
    
    // Gestion plus précise des erreurs
    if (error.response?.status === 401) {
      apiError.value = "Identifiants invalides. Veuillez vérifier votre nom d'utilisateur et mot de passe.";
    } else if (error.response?.status === 400) {
      apiError.value = "Votre profil est incomplet. Veuillez finaliser votre inscription.";
    } else if (error.response?.status === 403) {
      apiError.value = "Votre compte a été désactivé. Veuillez contacter l'administrateur.";
    } else {
      apiError.value = "Une erreur est survenue lors de la connexion. Veuillez réessayer plus tard.";
    }
  } finally {
    isLoading.value = false;
  }
};
onMounted(() => {
  document.body.classList.add("about-us", "bg-white");

  // Check if user email was remembered
  const rememberedEmail = localStorage.getItem('userEmail');
  if (rememberedEmail) {
    username.value = rememberedEmail;
    rememberMe.value = true;
  }
});

onUnmounted(() => {
  document.body.classList.remove("about-us", "bg-white");
});
</script>

<style scoped>
.login-page {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.login-container {
  width: 450px;
  background: #fff;
  padding: 40px;
  border-radius: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.form-group {
  margin-bottom: 20px;
  text-align: left;
}

.form-group input {
  width: 100%;
  padding: 8px;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 7px;
}

.error {
  color: red;
  font-size: 12px;
  margin-top: 5px;
}

.error-input {
  border-color: #ff4444;
}

.error-message {
  color: #ff4444;
  margin-top: 10px;
  text-align: center;
}

.form-options {
  display: flex;
  justify-content: space-between;
  margin: 18px 0;
}

.forgot-password {
  color: #5d6c8d;
  text-decoration: none;
}

.login-button {
  width: 100%;
  padding: 6px;
  background: #5d6c8d;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 14px;
}

.login-button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.footer-text {
  font-size: 14px;
  margin-top: 20px;
  color: #666;
}

.forget-text {
  font-size: 14px;
}

.footer-text a {
  color: #5d6c8d;
  text-decoration: none;
}

.text-btn {
  font-size: 12px;
}

label {
  font-size: 14px;
  display: block;
  margin-bottom: 5px;
}
</style>