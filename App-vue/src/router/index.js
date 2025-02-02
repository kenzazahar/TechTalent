import { createRouter, createWebHistory } from "vue-router";
import login from "../views/LandingPages/login.vue";
import AboutView from "../views/LandingPages/AboutView.vue";
import connexion from "../views/LandingPages/Connexion.vue";
import DocsEntretienEmbauche from "../views/LandingPages/DocsEntretienEmbauche.vue";
import DocsTendancesEmploi from "../views/LandingPages/DocsTendancesEmploi.vue";
import inscription_Candidat from "../views/LandingPages/inscription_Candidat.vue";
import inscription_Entreprise from "../views/LandingPages/inscription_Entreprise.vue";
import JobOffersDashboard from "../views/LandingPages/JobOffersDashboard.vue"; 
import NewOffer from "../views/LandingPages/NewOffer.vue";

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
      path: '/dashboard',  
      name: 'dashboard',
      component: JobOffersDashboard,
      
    },
    {
      path: '/company/profile',
      name: 'CompanyProfile',
      component: () => import('../views/LandingPages/CompanyProfile.vue')
    },
    {
      path: '/company/edit-profile',
      name: 'EditCompanyProfile',
      component: () => import('../views/LandingPages/EditCompanyProfile.vue')
    },
    
    {
      path: "/dashboard/offers/:id",
      name: "PublishOfferDetail",
      component: () => import("../views/LandingPages/PublishOfferDetail.vue"),
    },
    {
      path: '/dashboard/offers/:id/candidates',
      name: 'CandidatesList',
      component: () => import('../views/LandingPages/ListCandidates.vue')
    },
    {
      path: '/dashboard/offers/:id/candidates/cv',
      name: 'CandidateCV',
      component: () => import('../views/LandingPages/CandidateCV.vue')
    },
    {
      path: "/dashboard/offers/:id/edit",
      name: "EditOffer",
      component: () => import("../views/LandingPages/EditOffer.vue"),
    },
    {
      path: "/dashboard/drafts/:id/edit",
      name: "EditDraft",
      component: () => import("../views/LandingPages/EditDraft.vue"),
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
      path: '/inscription-candidat',  // URL plus simple et plus claire
      name: 'inscription_Candidat',
      component: inscription_Candidat,
    },
    {
      path: '/pages/landing-pages/inscription_Entreprise',
      name: 'inscription_Entreprise',
      component: inscription_Entreprise,
    },
    {
      path: "/dashboard/new-offer",
      name: "NewOffer",
      component: NewOffer,
    },
    {
      path: '/candidate/dashboard',
      name: 'candidateDashboard',
      component: () => import('../views/LandingPages/CandidateDashboard.vue')
    },
    {
      path: '/candidate/dashboard/profile',
      name: 'CandidateProfile',
      component: () => import('../views/LandingPages/ProfileCandidat.vue')
    },
    {
      path: '/candidate/dashboard/edit-profile',
      name: 'EditCandidateProfile',
      component: () => import('../views/LandingPages/EditProfileCandidate.vue')
    },
    {
      path: '/candidate/dashboard/applications',
      name: 'candidateApplications',
      component: () => import('../views/LandingPages/CandidateApplications.vue')
    },
    {
      path: '/dashboard/applications',
      name: 'MyApplications',
      component: () => import('../views/LandingPages/ListApplications.vue')
    },
    {
      path: '/candidate/dashboard/offers/:id',
      name: "OfferDetail",
      component: () => import('../views/LandingPages/OfferDetail.vue'),
    }
  ],
});



export default router;