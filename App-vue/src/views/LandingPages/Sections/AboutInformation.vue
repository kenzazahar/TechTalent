<script setup>
// example components
import DefaultInfoCard from "../cards/infoCards/DefaultInfoCard.vue";
import CenteredBlogCard from "../cards/blogCards/CenteredBlogCard.vue";
import recrutement from "@/assets/img/recrutement.jpg";
</script>
<template>
  <section class="py-5">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-10 mx-auto  text-center py-1">
          <h3 class="mb-0">Transformez votre Recrutement avec TechTalent</h3>
        </div>
        <div class="col-lg-7  ms-6 me-auto p-lg-3 mt-lg-2">
          <div class="row justify-content-start">
            <DefaultInfoCard
              color="info"
              icon="apps"
              title="Créer une Offre"
              description="Rendez vos offres de stage et d'emploi visibles auprès des talents adaptés, en quelques clics."
              />
            <DefaultInfoCard
              color="info"
              icon="3p"
              title="Gérer les Candidatures"
              description="Accédez à un tableau de bord intuitif pour filtrer, analyser et organiser les candidatures en toute simplicité."
            />
          </div>
          <div class="row justify-content-start mt-4">
            <DefaultInfoCard
              color="info"
              icon="public"
              title="Partager vos Offres"
              description="Diffusez vos annonces à un large public en les partageant directement sur les principales plateformes sociales."
            
            />
            <DefaultInfoCard
              color="info"
              icon="payments"
              title="Suivi Collaboratif"
              description="Facilitez les échanges entre recruteurs en ajoutant des commentaires et notes collaboratives sur les candidat."
            />
          </div>
        </div>
        <div class="col-lg-3 mt-lg-1 mt-8 col-lg-4 me-4 p-lg-5 mt-lg-4">
          <CenteredBlogCard
            :image="recrutement"
            title="Simplifiez Votre Recrutement"
            description="Rejoignez TechTalent pour accélérer votre processus de recrutement et identifier les talents idéaux en un clin d'œil."
            />
        </div>
      </div>
    </div>
  </section>
</template>