<script setup>
import logoDark from "@/assets/img/logo-removebg-preview.png";
import MaterialSocialButton from "../components/MaterialSocialButton.vue";

defineProps({
  brand: {
    type: Object,
    name: String,
    logo: String,
    route: "",
    default: () => ({
      name: "TechTalent",
      logo: logoDark,
      route: "/"
    })
  },
  socials: {
    type: Array,
    icon: String,
    link: String,
    default: () => [
      {
        icon: '<i class="fab fa-facebook text-lg opacity-8"></i>',
        link: "https://www.facebook.com/CreativeTim/"
      },
      {
        icon: '<i class="fab fa-twitter text-lg opacity-8"></i>',
        link: "https://twitter.com/creativetim"
      },
      {
        icon: '<i class="fab fa-dribbble text-lg opacity-8"></i>',
        link: "https://dribbble.com/creativetim"
      },
      {
        icon: '<i class="fab fa-github text-lg opacity-8"></i>',
        link: "https://github.com/creativetimofficial"
      },
      {
        icon: '<i class="fab fa-youtube text-lg opacity-8"></i>',
        link: "https://www.youtube.com/channel/UCVyTG4sCw-rOvB9oHkzZD1w"
      }
    ]
  },
  menus: {
    type: Array,
    name: String,
    items: {
      type: Array,
      name: String,
      href: String
    },
    default: () => [
      {
        name: "company",
        items: [
          {
            name: "about us",
            href: "https://www.creative-tim.com/presentation"
          },
          {
            name: "freebies",
            href: "https://www.creative-tim.com/templates/free"
          },
         ]
      },
      {
        name: "resources",
        items: [
          { name: "illustrations", href: "https://iradesign.io/" },
          {
            name: "bits & snippets",
            href: "https://www.creative-tim.com/bits"
          },
        ]
      },
      {
        name: "help & support",
        items: [
          {
            name: "contact us",
            href: "https://www.creative-tim.com/contact-us"
          },
          {
            name: "knowledge center",
            href: "https://www.creative-tim.com/knowledge-center"
          },
        ]
      },
    ]
  }
});
</script>
<template>
  <footer class="footer pt-0 mt-0">

    <div class="py-6">
      <div class="container">
        <div class="row d-flex justify-content-between align-items-center">
          <!-- Menu à gauche -->
          <div class="col-lg-7 col-md-10" style="margin-top: 45px;">
            <div class="row">
              <!-- Logo et Réseaux sociaux -->
              <div class="col-md-3 mb-3 ms-0">
                <div style="text-align: center;">
                  <a :href="brand.route">
                    <img src="@/assets/img/logo-removebg-preview.png" style="width: 100px;" class="img-fluid">
                  </a>
                  </div>
                <div>
                  <ul class="d-flex flex-row ms-n3 nav">
                    <li
                      class="nav-item"
                      v-for="{ icon, link } of socials"
                      :key="link"
                    >
                      <a
                        class="nav-link pe-1"
                        :href="link"
                        target="_blank"
                        v-html="icon"
                      >
                      </a>
                    </li>
                  </ul>
                </div>
              </div>

              <!-- Menus -->
              <div class="col-md-9">
                <div class="row">
                  <div
                    class="col-md-4 col-sm-6 col-8 mb-4"
                    v-for="(menu, index) in menus"
                    :key="index"
                  >
                    <h6 class="text-sm">{{ menu.name }}</h6>
                    <ul class="flex-column ms-n3 nav">
                      <li class="nav-item" v-for="(item, itemIndex) in menu.items" :key="itemIndex">
                        <a class="nav-link" :href="item.href" target="_blank">
                          {{ item.name }}
                        </a>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- "Thank you for your support!" à droite -->
          <div class="col-lg-5 col-md-6 text-end ">
            <h4 class="mb-3">Thank you for your support!</h4>
            <div class="social-icons mt-3">
              <MaterialSocialButton
                route="https://twitter.com/intent/tweet?text=Check%20Material%20Design%20System%20made%20by%20%40CreativeTim%20%23webdesign%20%23designsystem%20%23bootstrap5&url=https%3A%2F%2Fwww.creative-tim.com%2Fproduct%2Fmaterial-design-system-pro"
                component="twitter"
                color="twitter"
                label="Tweet"
              />
              <MaterialSocialButton
                route="https://www.facebook.com/sharer/sharer.php?u=https://www.creative-tim.com/product/material-design-system-pro"
                component="facebook-square"
                color="facebook"
                label="Share"
              />
              <MaterialSocialButton
                route=""
                component="pinterest"
                color="pinterest"
                label="Pin it"
              />
            </div>
          </div>

          <!-- Section copyright -->
          <div class="col-12">
            <div class="text-center">
              <p class="text-dark my-4 text-sm font-weight-normal">
                All rights reserved. Copyright ©
                {{ new Date().getFullYear() }}
                Material Kit by
                <a href="https://www.creative-tim.com" target="_blank"
                  >Creative Tim</a
                >.
              </p>
            </div>
          </div>
          
        </div>
      </div>
    </div>

    


  </footer>
</template>
