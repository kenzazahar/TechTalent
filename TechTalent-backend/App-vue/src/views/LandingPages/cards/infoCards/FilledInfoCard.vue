<script setup>
defineProps({
  color: {
    text: String,
    background: {
      validator(value) {
        return [
          "primary",
          "secondary",
          "info",
          "success",
          "warning",
          "error",
          "light",
          "dark",
          "white",
        ].includes(value);
      },
    },
    default() {
      return {
        text: "",
        background: "bg-gray-100",
      };
    },
  },
  icon: {
    type: Object,
    required: true,
    component: String,
    color: String,
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
    required: true,
    label: {
      type: Object,
      required: true,
      text: String,
      color: String,
    },
    route: {
      type: String,
      required: true,
    },
  },
});
</script>
<template>
  <div
    class="info-horizontal border-radius-xl d-block d-md-flex"
    :class="`${color.background ?? ''}`"
  >
    <i class="material-icons text-3xl" :class="`text-${icon.color}`">{{
      icon.component
    }}</i>
    <div class="ps-0 ps-md-3 mt-3 mt-md-0">
      <h6 :class="`text-${color.text ?? ''}`">{{ title }}</h6>
      <p :style="{ fontSize: '13px' }" :class="`text-${color.text ?? ''}`">
        {{ description }}
      </p>
      
    </div>
  </div>
</template>
