<script setup>
defineProps({
  image: {
    type: String,
    required: true,
  },
  title: {
    type: String,
    required: true,
  },
  description: {
    type: String,
    required: true,
  },
  action: {
    type: Object,
    color: String,
    route: String,
    label: String,
    default: () => ({
      color: "bg-gradient-secondary .multisteps-form__progress-btn:before",
      label: "Inscription Entreprise",
    }),
  },
});
</script>
<template>
  <div class="card">
    <div class="card-header p-0 position-relative mt-n4 mx-1 z-index-3">
      <a :href="action.route" class="d-block blur-shadow-image">
        <img :src="image" :alt="title" class="img-fluid border-radius-lg" />
      </a>
    </div>
    <div class="card-body text-center">
      <h6 class="font-weight-normal">
        <a href="javascript:;">{{ title }}</a>
      </h6>
      <p :style="{ fontSize: '12px' }"  class="mb-0">
        {{ description }}
      </p>
      <RouterLink to="/pages/landing-pages/inscription_Entreprise" type="button" class="btn btn-sm mb-0 mt-3" style=" width: 150px; height: 31px; font-size: 9px;  align-items: center; justify-content: center;" :class="action.color">
        {{ action.label }}
      </RouterLink>
    </div>
  </div>
</template>
