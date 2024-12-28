import { createRouter, createWebHistory } from "vue-router";
import login from "../views/LandingPages/login.vue";
import AboutView from "../views/LandingPages/AboutView.vue";
import connexion from "../views/LandingPages/Connexion.vue";
import DocsEntretienEmbauche from "../views/LandingPages/DocsEntretienEmbauche.vue";
import DocsTendancesEmploi from "../views/LandingPages/DocsTendancesEmploi.vue";
import inscription_Candidat from "../views/LandingPages/inscription_Candidat.vue";
import inscription_Entreprise from "../views/LandingPages/inscription_Entreprise.vue";


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "about",
      component: AboutView,
    },
    {
      path: '/connexion',
      name: 'connexion',
      component: connexion,
    },
    {
      path: '/login',
      name: 'login',
      component: login,
    },
    {
      path: '/pages/landing-pages/Docs',
      name: 'DocsEntretienEmbauche',
      component: DocsEntretienEmbauche,
    },
    {
      path: '/pages/landing-pages/Docs',
      name: 'DocsTendancesEmploi',
      component: DocsTendancesEmploi,
    },
    {
      path: '/pages/landing-pages/inscription_Candidat',
      name: 'inscription_Candidat',
      component: inscription_Candidat,
    },
    {
      path: '/pages/landing-pages/inscription_Entreprise',
      name: 'inscription_Entreprise',
      component: inscription_Entreprise,
    }
  ],
});

export default router;  
