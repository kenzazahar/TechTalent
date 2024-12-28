<script setup>
// example component
import DefaultCounterCard from "../cards/counterCards/DefaultCounterCard.vue";
</script>
<template>
  <section class="pt-4 pb-6" id="count-stats">
    <div class="container">
      <div class="row justify-content-center text-center">
        <div class="col-md-3">
          <DefaultCounterCard
            title="Entreprises"
            description="Nombre total d'entreprises collaborant avec notre plateforme"
            :count="1234"
            :duration="3000"
          />
        </div>
        <div class="col-md-3">
          <DefaultCounterCard
            title="Candidats"
            description="Nombre de candidats inscrits et actifs sur notre plateforme"
            :count="3423"
            :duration="3000"
          />
        </div>
        <div class="col-md-3">
          <DefaultCounterCard
            title="Offres"
            description="Nombre d'offres d'emploi actuellement disponibles"
            :count="7568"
            :duration="4000"
          />
        </div>
      </div>
    </div>
  </section>
</template>
