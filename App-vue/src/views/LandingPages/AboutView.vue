<script setup>
import { onMounted, onUnmounted } from "vue";

//components
import DefaultNavbar from "./navbars/NavbarDefaults.vue";
import DefaultFooter from "./footers/FooterDefault.vue";
import FilledInfoCard from "./cards/infoCards/FilledInfoCard.vue";
import TransparentBlogCard from "./cards/blogCards/TransparentBlogCard.vue";
import MaterialInput from "./components/MaterialInput.vue";
import MaterialTextArea from "./components/MaterialTextArea.vue";
import Information from "./Sections/AboutInformation.vue";
import Featuring from "./Sections/AboutFeaturing.vue";
import MaterialButton from "./components/MaterialButton.vue";
import setMaterialInput from "@/assets/js/material-input";

//image
import bg0 from "@/assets/img/bg91.jpg";
import post1 from "@/assets/img/examples/localisation.jpg";
import post2 from "@/assets/img/examples/domaine.jpg";
import post3 from "@/assets/img/examples/Competence.jpg"; 
import post4 from "@/assets/img/examples/Contrat.jpg"; 
import bgContact from "@/assets/img/Informatique.png";


// store
import { useAppStore } from "@/stores";
const store = useAppStore();

//dep
import Typed from "typed.js";

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

defineProps({
  action: {
    type: Object,
    color: String,
    route: String,
    label: String,
    default: () => ({
      color: "bg-gradient-secondary .multisteps-form__progress-btn:before",
      label: "Inscription Candidat",
    })
  }
})
</script>
<template>
  <DefaultNavbar
    :action="{
      route: 'javascript:;',
      label: 'Buy Now',
      color: 'btn-white',
    }"
    transparent
  />
  <header class="bg-gradient-dark">
    <div
      class="page-header min-vh-75"
      :style="{ backgroundImage: `url(${bg0})` }"
    >
      <span class="mask bg-gradient-dark opacity-6"></span>
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-9 text-center mx-auto my-auto">
            <h3 class="text-white">
              Votre avenir commence avec <span class="text-white" id="typed"></span>
            </h3>
            <div id="typed-strings">
              <h3>Inspiration</h3>
              <h3>Excellence</h3>
              <h3>Innovation</h3>
            </div>
            <p class="lead mb-2 text-white opacity-8 custom-text-sizes">
              Rejoignez TechTalent, la plateforme qui transforme les ambitions en réalisations.
            </p>
            <p class="lead mb-4 text-white opacity-8 custom-text-sizes">
              Découvrez, connectez, réussissez !
            </p>
            <RouterLink to="/pages/landing-pages/inscription_Candidat" class="btn bg-white text-dark mx-2" style=" width: 150px; height: 31px; font-size: 9px;  align-items: center; justify-content: center;">
              Inscription Candidat
            </RouterLink>
          <RouterLink to="/pages/landing-pages/inscription_Entreprise" class="btn bg-white text-dark mx-2" style=" width: 158px; height: 31px; font-size: 9px;  align-items: center; justify-content: center;">
            Inscription Entreprise
          </RouterLink>
          </div>
        </div>
      </div>
    </div>
  </header>

  <div class="card card-body shadow-xl mx-3 mx-md-4 mt-n6">
    <section class="py-5"></section>
    <div class="container">
      <div class="row">
        <div class="col-lg-10 mx-auto  text-center">
          <h3 class="mb-0">Bienvenue sur TechTalent</h3>
          <p class="py-3 custom-text-size">
            TechTalent réinvente le recrutement dans le secteur informatique en offrant une plateforme performante et flexible, pensée pour répondre aux besoins spécifiques des entreprises à la recherche de talents, ainsi que des candidats en quête de nouvelles opportunités professionnelles. Grâce à une architecture logicielle moderne, TechTalent optimise la gestion des candidatures et des offres d’emploi, tout en assurant une expérience utilisateur fluide et intuitive. Le design de la plateforme facilite une navigation sans effort, permettant à chaque utilisateur de trouver rapidement ce qu’il cherche, qu’il s’agisse de talents ou de nouvelles opportunités. Conçue sur des bases solides et intégrant des technologies de pointe, la plateforme garantit une performance optimale et une capacité d’adaptation parfaite, capable de suivre la croissance des entreprises tout en répondant aux aspirations des candidats.
          </p>
        </div>
      </div>
    </div>
    <Information />

    <section class="py-2"></section>
    <div class="container">
      <div class="row">
        <div class="col-lg-7 mx-auto  text-center">
          <h3 class="mb-0 " >Votre Avenir Commence Ici</h3>
          <h4 class="py-1 text-gradient bg-gradient-secondary .multisteps-form__progress-btn:before mb-2">
            Trouvez le Stage ou l'Emploi de Vos Rêves
          </h4>
          <p class="custom-text-size-critere">
            Étudiants et diplômés, préparez-vous à transformer votre carrière. Des opportunités sur mesure, juste pour vous. 
          </p>
          <RouterLink to="/pages/landing-pages/inscription_Candidat"  type="button" class="btn btn-sm mb-0 mt-1" style=" width: 150px; height: 30px; font-size: 9px;  align-items: center; justify-content: center;" :class="action.color">
                {{ action.label }}
          </RouterLink>
        </div>
      </div>
    </div>

    <section class="py-3"></section>
    <div class="container">
      <div class="row"> 
        <div class="col-lg-4">
          <FilledInfoCard
            class="px-lg-1 mt-lg-0 mt-4 p-4"
            height="h-100"
            :icon="{ component: '', color: 'bg-gradient-secondary .multisteps-form__progress-btn:before' }"
            title="Lancez Votre Aventure"
            description="Créez un profil unique qui reflète vos compétences, vos expériences et vos aspirations professionnelles. Profitez d’un espace dédié pour mettre en avant vos atouts et démarquez-vous auprès des recruteurs."
            :action="{
              route:
                'https://www.creative-tim.com/learning-lab/vue/overview/material-kit/',
              label: { text: 'Let\'s start', color: 'dark' }
            }"
          />
        </div>
        <div class="col-lg-4">
          <FilledInfoCard
            class="px-lg-1 mt-lg-0 mt-4 p-4"
            height="h-100"
            :icon="{ component: '', color: 'bg-gradient-secondary .multisteps-form__progress-btn:before' }"
            title="Des Opportunités Qui Vous Ressemblent"
            description=" Explorez un large éventail d'offres adaptées à vos compétences et à vos objectifs. Que vous soyez étudiant ou diplômé, trouvez des stages, emplois ou projets alignés avec vos ambitions."
            :action="{
              route:
                'https://www.creative-tim.com/learning-lab/vue/overview/material-kit/',
              label: { text: 'Let\'s start', color: 'dark' }
            }"
          />
        </div>
        <div class="col-lg-4">
          <FilledInfoCard
            class="px-lg-1 mt-lg-0 mt-4 p-4"
            height="h-100"
            :icon="{ component: '', color: 'bg-gradient-secondary .multisteps-form__progress-btn:before' }"
            title="Transformez Vos Rêves en Réalité"
            description="Passez à l’action avec des outils simplifiés pour postuler directement aux offres qui vous correspondent.  Suivez vos candidatures et recevez des notifications pour avancer vers vos ambitions."
            :action="{
              route:
                'https://www.creative-tim.com/learning-lab/vue/overview/material-kit/',
              label: { text: 'Let\'s start', color: 'dark' }
            }"
          />
        </div>
      </div>
    </div>

    <section class="py-4"></section>
    <section class="py-sm-3 py-5 position-relative">
    <div class="container">
      <div class="row">
        <div class="col-12 mx-auto">
          <div class="row py-5">
            <div
              class="col-lg-9 col-md-7 z-index-2 position-relative px-md-2 px-sm-5 mx-auto mb-2 col-lg-5 mx-auto  text-center"
            >
              <div
                class="d-flex justify-content-between align-items-center mb-2 col-lg-8 mx-auto  text-center"
              >
                <h3 class="mb-0">Explorez nos offres d'emploi et de stage</h3>
              </div>
              <p class="mb-0 custom-text-size-critere">
                Découvrez les opportunités professionnelles que nous proposons dans différents domaines
                 technologiques. Que vous soyez candidat à la recherche de votre premier emploi ou une 
                 entreprise en quête de talents, nous avons une offre adaptée à vos besoins. Vous pouvez 
                 filtrer les offres selon des critères clés pour trouver celle qui vous correspond le mieux.
                <br />
              </p>
            </div>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-lg-6">
          <h3 class="mb-4">Critères de Recherche</h3>
        </div>
      </div>
      <div class="row">
        <div class="col-lg-3 col-sm-6">
          <TransparentBlogCard
            :image="post1"
            title="Localisation"
            description="Filtrez les offres selon la zone géographique qui vous intéresse. Que vous recherchiez un poste local ou une opportunité à distance, la localisation vous aide à trouver des offres adaptées à vos préférences."
          />
        </div>
        <div class="col-lg-3 col-sm-6">
          <TransparentBlogCard
            :image="post2"
            title="Domaine d'activité"
            description="Sélectionnez votre spécialisation parmi des secteurs tels que le développement web, la data science ou la cybersécurité pour trouver des offres correspondant à vos compétences techniques."
          />
        </div>
        <div class="col-lg-3 col-sm-6">
          <TransparentBlogCard
            :image="post3"
            title="Compétences requises"
            description="Recherchez des offres adaptées à vos compétences, que ce soit en gestion de projet, programmation ou analyse de données, pour mieux cibler des opportunités correspondant à vos qualifications."
          />
        </div>
        <div class="col-lg-3 col-sm-6">
          <TransparentBlogCard
          :image="post4"
            title="Type de contrat"
            description="Choisissez le type de contrat qui correspond à vos objectifs professionnels, que ce soit un CDI, un CDD, un stage, ou une mission freelance. Ce critère vous permet de définir votre engagement à court ou long terme."
          />
        </div>
       
      </div>
    </div>
    </section>

    <section class="py-4"></section>
    <div class="section section-team text-center">
      <div class="container">
        <h3 class="title">Voici notre équipe</h3>
        <div class="team">
          <div class="row py-4">
            <div class="col-md-4">
              <div class="team-player">
                <img src="@/assets/img/photo.jpg"
                  class="rounded-circle img-center img-fluid shadow shadow-lg--hover"
                  style="width: 140px;"
                  alt="Description de l'image">
                  <h5 class="title py-2"></h5>
                <h5 class="title">Soulhi Malak</h5>
                <p class=" text-dark custom-text-size-critere">Élève ingénieur</p>
                <p class="description custom-text-size-team">
                  You can write here details about one of your team members. You
                  can give more details about what they do. Feel free to add
                  some <a href="#">links</a> for people to be able to follow
                  them outside the site.
                </p>
              </div>
            </div>
            <div class="col-md-4">
              <div class="team-player">
                <img src="@/assets/img/photo_kenza.jpg"
                  class="rounded-circle img-center img-fluid shadow shadow-lg--hover"
                  style="width: 140px;"
                  alt="Description de l'image">
                  <h5 class="title py-2"></h5>
                <h5 class="title">Zahar Kenza</h5>
                <p class="text-dark custom-text-size-critere">Élève ingénieur</p>
                <p class="description custom-text-size-team">
                  You can write here details about one of your team members. You
                  can give more details about what they do. Feel free to add
                  some <a href="#">links</a> for people to be able to follow
                  them outside the site.
                </p>
              </div>
            </div>
            <div class="col-md-4">
              <div class="team-player">
                <img src="@/assets/img/photo_firdaous.jpg"
                  class="rounded-circle img-center img-fluid shadow shadow-lg--hover"
                  style="width: 140px;"
                  alt="Description de l'image">
                <h5 class="title py-2"></h5>
                <h5 class="title">Souidak Firdaous</h5>
                <p class="text-dark custom-text-size-critere">Élève ingénieur</p>
                <p class="description custom-text-size-team">
                  You can write here details about one of your team members. You
                  can give more details about what they do. Feel free to add
                  some <a href="#">links</a> for people to be able to follow
                  them outside the site.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <section class="py-5"></section>
    <section class="py-lg-1">
    <div class="container">
      <div class="row mx-3 ms-3">
        <div class="col">
          <div class="card box-shadow-x1 overflow-hidden mb-">
            <div class="row">
              <div
                class="col-lg-5 position-relative bg-cover px-0"
                :style="{ backgroundImage: `url(${bgContact})` }"
                loading="lazy"
              >
                <div
                  class="z-index-1 text-center d-flex h-50 w-100 d-flex justify-content-center"
                >
                  <div class="mask bg-gradient-dark opacity-8"></div>
                  <div
                    class="p-6 ps-sm-7 position-relative text-start my-auto z-index-2"
                  >
                  <section class="py-6"></section>
                    <h5 class="text-white">Informations de Contact</h5>
                    <p class="text-white opacity-8 mb-3 custom-text-size-team">
                      Veuillez remplir ce formulaire. Notre équipe vous répondra dans un délai de 24 heures.
                    </p>
                    <div class="d-flex p-2 text-white">
                      <div>
                        <i class="fas fa-phone text-sm"></i>
                      </div>
                      <div class="ps-3">
                        <span class="text-sm opacity-8">(+212) 620655986</span>
                      </div>
                    </div>
                    <div class="d-flex p-2 text-white">
                      <div>
                        <i class="fas fa-envelope text-sm"></i>
                      </div>
                      <div class="ps-3">
                        <span class="text-sm opacity-8"
                          >TechTalent@gmail.com</span
                        >
                      </div>
                    </div>
                    <div class="d-flex p-2 text-white">
                      <div>
                        <i class="fas fa-map-marker-alt text-sm"></i>
                      </div>
                      <div class="ps-3">
                        <span class="text-sm opacity-8"
                          >Tanger, Maroc</span
                        >
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-7">
                <form class="" id="contact-form" method="post">
                  <div class="card-header px-4 py-sm-4">
                    <h3>Formulaire de Contact</h3>
                    <p class="custom-text-size-Cantact">Merci de nous transmettre vos questions ou remarques.</p>
                  </div>
                  <div class="card-body pt-1">
                    <div class="row">
                      <div class="col-md-12 pe-0 mb-3">
                        <MaterialInput
                          class="input-group-static mb-3"
                          label="Nom complet"
                          type="text"
                          placeholder="Entrez votre nom complet"
                        />
                      </div>
                      <div class="col-md-12 pe-0 mb-3">
                        <MaterialInput
                          class="input-group-static mb-4"
                          label="Sujet de la demande"
                          type="text"
                          placeholder="Décrivez l'objet de votre message"
                        />
                      </div>
                      <div class="col-md-12 pe-0 mb-3">
                        <MaterialTextArea
                          class="input-group-static mb-3"
                          placeholder="Écrivez votre message ici"
                          :rows="4"
                          >Votre message</MaterialTextArea
                        >
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-md-4 text-end ms-auto">
                        <MaterialButton
                          variant="gradient"
                          color="dark"
                          type="submit"
                          class="mb-0"
                          >Envoyer</MaterialButton
                        >
                      </div>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    </section>

    <section class="py-5"></section>
    <Featuring />
  </div>
    <DefaultFooter />
</template>

<style scoped>
.text-noir {
  color: #333333; /* Noir */
}
.custom-text-size {
  font-size: 0.84rem; /* Par exemple, une taille de texte plus petite que .lead */
}
.custom-text-sizes {
  font-size: 1.03rem; /* Par exemple, une taille de texte plus petite que .lead */
}
.custom-text-size-critere {
  font-size: 15px; /* Par exemple, une taille de texte plus petite que .lead */
}
.custom-text-size-team {
  font-size: 14px; /* Par exemple, une taille de texte plus petite que .lead */
}
.custom-text-size-Contact {
  font-size: 16px; /* Par exemple, une taille de texte plus petite que .lead */
}
</style>