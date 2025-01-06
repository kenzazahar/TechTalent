<script setup>
import { onMounted, onUnmounted } from "vue";

//example components
import DefaultNavbar from "./navbars/NavbarDefaults.vue";
import DefaultFooter from "./footers/FooterDefault.vue";


// store
import { useAppStore } from "@/stores";
const store = useAppStore();

//dep
import Typed from "typed.js";
import setMaterialInput from "@/assets/js/material-input";
onMounted(() => {
  setMaterialInput();
});

const body = document.getElementsByTagName("body")[0];
//hooks
onMounted(() => {
  body.classList.add("about-us");
  body.classList.add("bg-gray-200");

  if (document.getElementById("typed")) {
    // eslint-disable-next-line no-unused-vars
    var typed = new Typed("#typed", {
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
  body.classList.remove("bg-gray-200");
});
</script>
<template>
  
  <header class="bg-gradient-white">
    <div
      class="page-header min-vh-60" 
    >
      <span class="mask bg-gradient-white opacity-6"></span>
      <div class="container">
        <DefaultNavbar />
      </div>
    </div>
  </header>

  <div class="card card-body shadow-xl mx-3 mx-md-3 mt-n6 pb-6">

    <section class="py-1"></section>
    <div class="row">
        <div class="col-11 mx-auto">
          <div class="row">
            <div
              class="col-lg-7 col-md-7 z-index-2 position-relative px-md-2 px-sm-2 mx-auto mb-2 col-lg-8 text-center"
            >
              <div
                class="d-flex justify-content-between align-items-center mb-2 col-lg-10 mx-auto  text-center"
              >
                <h3 class="mb-0">Bienvenue dans votre espace d'inscription</h3>
              </div>
              <p class="mb-0">
                Rejoignez notre plateforme pour découvrir des opportunités uniques adaptées à vos besoins. 
                Que vous soyez candidat ou entreprise, accédez à un espace personnalisé pour simplifier vos démarches 
                et atteindre vos objectifs en toute simplicité.
              </p>
            </div>
          </div>
          <div class="container">
          <div class="row justify-content-center">
            <div class="col-md-4">
              <!-- Card pour l'inscription Candidat -->
              <div class="card mb-4 shadow-sm">
                <img
                  src="@/assets/img/Inscription_Candidat.jpg"
                  class="card-img-top"
                  alt="Candidat"
                />
                <div class="card-body">
                  <h5 class="card-title">Inscription Candidat</h5>
                  <p class="card-text">
                    Créez votre profil pour postuler à des offres de recrutement.
                  </p>
                  <RouterLink to="/pages/landing-pages/inscription_Candidat" class="btn btn-dark" >
                    S'inscrire en tant que Candidat
                  </RouterLink>
                </div>
              </div>
            </div>

            <div class="col-md-4">
              <!-- Card pour l'inscription Entreprise -->
              <div class="card mb-4 shadow-sm">
                <img
                  src="@/assets/img/Inscription_Entreprise.jpg"
                  class="card-img-top"
                  alt="Entreprise"
                />
                <div class="card-body">
                  <h5 class="card-title">Inscription Entreprise</h5>
                  <p class="card-text">
                    Créez un compte entreprise pour publier des offres et gérer vos candidatures.
                  </p>
                  <RouterLink to="/pages/landing-pages/inscription_Entreprise"  class="btn btn-dark">
                    S'inscrire en tant qu'Entreprise
                  </RouterLink>
                  
                </div>
              </div>
            </div>

          </div>
        </div>
        </div>
      </div>

  </div>
  <DefaultFooter />
</template>

<style scoped>
.container {
  margin-top: 50px;
}

.card {
  border-radius: 15px;
}

.card-img-top {
  height: 200px;
  object-fit: cover;
}

.card-body {
  text-align: center;
}

.card-title {
  font-weight: bold;
  font-size: 1.3rem;
}

.card-text {
  font-size: 1rem;
}

.btn {
  width: 100%;
}

.row {
  margin-top: 70px;
  gap: 50px;
}
</style>
