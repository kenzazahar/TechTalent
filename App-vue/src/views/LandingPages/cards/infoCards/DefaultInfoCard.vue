<script setup>
defineProps({
  icon: {
    type: [String, Object],
    default: "",
    component: String,
    size: String,
    color: String,
  },
  image: {
    type: Object,
    component: String,
    class: String,
    default: () => {},
  },
  title: {
    type: [String, Object],
    required: true,
    text: String,
    class: String,
  },
  description: {
    type: [String, Object],
    required: true,
    text: String,
    class: String,
  },
  col: {
    type: String,
    default: "",
  },
});
</script>
<script>
export default {
  inheritAttrs: false,
};
</script>
<template>
  <div :class="`${col ? col : 'col-md-6'}`">
    <div v-bind="$attrs" class="info">
      <i
        v-if="icon"
        class="material-icons text-gradient"
        :class="`${
          typeof icon == 'object'
            ? `text-${icon.color} text-${icon.size}`
            : 'bg-gradient-secondary .multisteps-form__progress-btn:before text-3xl'}`"
        :style="{ fontSize: '30px' }"
        >{{ typeof icon == "object" ? icon.component : icon }}</i
      >
      <img v-if="image" :src="image.component" :class="image.class" />
      <h6
        :class="
          typeof title == 'string' ? 'font-weight-bolder mt-1' : title.class
        "
      >
        {{ typeof title == "string" ? title : title.text }}
      </h6>
      <p :style="{ fontSize: '13px' }" :class="typeof description == 'string' ? 'pe-5' : description.class">
        {{ typeof description == "string" ? description : description.text }}
      </p>
    </div>
  </div>
</template>