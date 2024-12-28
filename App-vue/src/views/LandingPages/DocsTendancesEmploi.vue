<script setup>
import { onMounted, onUnmounted } from "vue";

//example components
import DefaultNavbar from "./navbars/NavbarDefaults.vue";
import DefaultFooter from "./footers/FooterDefault.vue";

//dep
import Typed from "typed.js";

//images
import bg0 from "@/assets/img/bg93.jpg";


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
          <div class="col-lg-8 text-center mx-auto my-auto">
            <h1 class="text-white">
                Tendances emploi 2025  
            </h1>
            <p class="lead mb-4 text-white opacity-8">
                En 2025, certains métiers tech devraient connaître un essor spectaculaire, portés par des secteurs en plein boom . Ces domaines offrent des opportunités pour les talents prêts à saisir les enjeux technologiques de demain.    
            </p>
            </div>
          </div>
        </div>
    </div>
  </header>

 
  <div class="card card-body shadow-xl mx-3 mx-md-4 mt-n6">
    <section class="py-sm-3 position-relative">
    <div class="container">
      <div class="row">
        <div class="col-15 mx-auto">
          <div class="row py-6">
            <div
              class="col-lg-10 col-md-7 z-index-2 position-relative px-md-2 px-sm-5 mx-8"
            >

        <div>
              <div
                class="d-flex justify-content-between align-items-center mb-2 py-2"
              >
                <h5 class="mb-0 text-noir ">Tendances emploi 2025</h5>
              </div>
              <div
                class="d-flex justify-content-between align-items-center mb-2 py-2 text-dark "
              >
                <h2 class="mb-0 text-noir ">Les métiers tech qui devraient exploser en 2025</h2>
              </div>
              <p class="text-lg mb-0 py-1 text-noir ">
                L’année 2025 s’annonce charnière pour le secteur de la tech. L’accélération des innovations post-pandémie, combinée à l’essor de l’intelligence artificielle, de la cybersécurité et des technologies durables, transforme le marché de l’emploi. De nouveaux métiers émergent tandis que certains rôles déjà établis prennent de plus en plus d'ampleur. Quels sont les métiers tech qui connaîtront une croissance explosive en 2025 ?
                <br />
              </p>
        </div>

        <div>
            <section class="py-4"></section>
            <div
                    class="d-flex justify-content-between align-items-center mb-2"
                >
                    <h2 class="mb-0 text-noir ">I. L’explosion de l’intelligence artificielle et ses métiers clés</h2>
            </div>
            <div>
                <section class="py-3"></section>
                <div
                        class="d-flex justify-content-between align-items-center mb-2"
                    >
                        <h3 class="mb-0 text-noir ">A. Ingénieur en IA & Machine Learning</h3>
                </div>
                <p class="text-lg mb-0 py-2 text-noir ">
                    Dans la continuité de ces dernières années, les entreprises investissent encore massivement dans l’intelligence artificielle pour automatiser leurs processus, optimiser la prise de décision et améliorer l’expérience utilisateur. Cela propulse naturellement la demande d’ingénieurs en IA et Machine Learning.
                    <br />
                </p>
                <section class="py-1"></section>
                <ul class="custom-list col-lg-11 col-md-9 z-index-2 position-relative px-md-0 px-sm-3 mx-6 mb-2 text-noir ">
                    <li>
                        Compétences recherchées : Programmation (Python, R), utilisation de frameworks IA comme TensorFlow et PyTorch, et expertise en data science.
                    </li>
                    <section class="py-1"></section>
                    <li>
                        Perspectives d’emploi : Selon l’OCDE, la croissance de ce métier pourrait atteindre +38 % d’ici 2025.
                    </li>
                    <section class="py-1"></section>
                    <li>
                        Salaire moyen : Entre 10 000 MAD et 40 000 MAD par an en fonction de l’expérience et de la taille de l’entreprise.
                    </li>
                </ul>
            </div>
            <div>
                <section class="py-3"></section>
                <div
                        class="d-flex justify-content-between align-items-center mb-2"
                    >
                        <h3 class="mb-0 text-noir ">B. Prompt Engineer (Ingénieur en création de prompts)</h3>
                </div>
                <p class="text-lg mb-0 py-2 text-noir ">
                    L’émergence des modèles génératifs tels que ChatGPT et DALL·E a donné naissance au métier de Prompt Engineer. Ces experts créent et optimisent des prompts (instructions textuelles) pour maximiser les performances des intelligences artificielles.
                    <br />
                </p>
                <section class="py-1"></section>
                <ul class="custom-list col-lg-11 col-md-9 z-index-2 position-relative px-md-0 px-sm-3 mx-6 mb-2 text-noir ">
                    <li>
                        Pourquoi ce métier explose ? Avec la popularité des IA conversationnelles et créatives, la maîtrise des prompts devient cruciale pour les entreprises souhaitant tirer profit de ces technologies.    
                    </li>
                </ul>
            </div>
 
 
        </div>

        <div>
            <section class="py-4"></section>
            <div
                    class="d-flex justify-content-between align-items-center mb-2"
                >
                    <h2 class="mb-0 text-noir ">II. La cybersécurité : un secteur toujours aussi clé</h2>
            </div>
            <div>
                <section class="py-3"></section>
                <div
                        class="d-flex justify-content-between align-items-center mb-2"
                    >
                        <h3 class="mb-0 text-noir ">A. Analyste en cybersécurité</h3>
                </div>
                <p class="text-lg mb-0 py-2 text-noir ">
                    La multiplication des cyberattaques et des violations de données pousse les entreprises à renforcer leur sécurité informatique. L’analyste en cybersécurité est au cœur de cette stratégie.
                    <br />
                </p>
                <section class="py-1"></section>
                <ul class="custom-list col-lg-11 col-md-9 z-index-2 position-relative px-md-0 px-sm-3 mx-6 mb-2 text-noir ">
                    <li>
                        Raison de la demande : Protéger les systèmes et les données sensibles face à des menaces de plus en plus sophistiquées.    
                    </li>
                    <section class="py-1"></section>
                    <li>
                        Chiffre clé : Le marché mondial de la cybersécurité devrait atteindre 376 milliards de dollars en 2025, selon Statista.   
                    </li>
                    <section class="py-1"></section>
                    <li>
                        Compétences : Gestion des incidents, mise en œuvre de normes de sécurité (ISO, NIST), maîtrise des logiciels de détection d’intrusion.   
                    </li>
                </ul>
            </div>
            <div>
                <section class="py-3"></section>
                <div
                        class="d-flex justify-content-between align-items-center mb-2"
                    >
                        <h3 class="mb-0 text-noir ">B. Responsable de la sécurité des systèmes d’information (RSSI)</h3>
                </div>
                <p class="text-lg mb-0 py-2 text-noir ">
                    Le RSSI joue un rôle stratégique en supervisant l’ensemble des politiques de sécurité informatique d’une organisation.
                    <br />
                </p>
                <section class="py-1"></section>
                <ul class="custom-list col-lg-11 col-md-9 z-index-2 position-relative px-md-0 px-sm-3 mx-6 mb-2 text-noir ">
                    <li>
                        Salaire moyen : Entre 80 000 € et 120 000 € par an en Europe, en fonction de la taille de l’entreprise.
                    </li>
                    <section class="py-1"></section>
                    <li>
                        Perspectives d’évolution : Avec l’intensification des menaces, ce poste devient de plus en plus crucial pour les grandes organisations. 
                    </li>

                </ul>
            </div>
 
 
        </div>

        <div>
            <section class="py-4"></section>
            <div
                    class="d-flex justify-content-between align-items-center mb-2"
                >
                    <h2 class="mb-0 text-noir ">III. La data : l’or noir du XXIe siècle</h2>
            </div>
            <div>
                <section class="py-3"></section>
                <div
                        class="d-flex justify-content-between align-items-center mb-2"
                    >
                        <h3 class="mb-0 text-noir ">A. Data Analyst & Data Scientist</h3>
                </div>
                <p class="text-lg mb-0 py-2 text-noir ">
                    Les données sont aujourd’hui l’une des ressources les plus précieuses pour les entreprises. Les Data Analysts et Data Scientists sont chargés de collecter, analyser et interpréter ces informations pour guider les décisions stratégiques.
                    <br />
                </p>
                <section class="py-1"></section>
                <ul class="custom-list col-lg-11 col-md-9 z-index-2 position-relative px-md-0 px-sm-3 mx-6 mb-2 text-noir ">
                    <li>
                        Compétences : Maîtrise des langages SQL, Python, R, et des outils de visualisation de données (Tableau, Power BI).    
                    </li>
                    <section class="py-1"></section>
                    <li>
                        Croissance de la demande : Une augmentation de +28 % d’ici 2025 en Europe est prévue, selon Eurostat.    
                    </li>
                    <section class="py-1"></section>
                    <li>
                        Salaire moyen : Entre 45 000 MAD et 85 000 MAD par an, selon l’expérience.   
                    </li>
                </ul>
            </div>
            <div>
                <section class="py-3"></section>
                <div
                        class="d-flex justify-content-between align-items-center mb-2"
                    >
                        <h3 class="mb-0 text-noir ">B. Ingénieur en Big Data</h3>
                </div>
                <p class="text-lg mb-0 py-2 text-noir ">
                    L’ingénieur en Big Data est responsable de la gestion et de l’exploitation des grands volumes de données générés par les entreprises.
                    <br />
                </p>
                <section class="py-1"></section>
                <ul class="custom-list col-lg-11 col-md-9 z-index-2 position-relative px-md-0 px-sm-3 mx-6 mb-2 text-noir ">
                    <li>
                        Marché : Selon l’IDC, le secteur du Big Data atteindra 103 milliards de dollars en 2025.    
                    </li>
                    <section class="py-1"></section>
                    <li>
                        Rôle clé : Concevoir des architectures de données robustes et optimisées pour analyser des volumes massifs d’informations.    
                    </li>

                </ul>
            </div>
 
 
        </div>

        <div>
            <section class="py-4"></section>
            <div
                    class="d-flex justify-content-between align-items-center mb-2"
                >
                    <h2 class="mb-0 text-noir ">IV. Le développement durable et la tech verte</h2>
            </div>
            <div>
                <section class="py-3"></section>
                <div
                        class="d-flex justify-content-between align-items-center mb-2"
                    >
                        <h3 class="mb-0 text-noir ">A. Ingénieur en technologies vertes</h3>
                </div>
                <p class="text-lg mb-0 py-2 text-noir ">
                    La transition vers un monde plus durable pousse les entreprises à intégrer des solutions technologiques écologiques. L’ingénieur en technologies vertes conçoit et met en œuvre ces innovations.
                    <br />
                </p>
                <section class="py-1"></section>
                <ul class="custom-list col-lg-11 col-md-9 z-index-2 position-relative px-md-0 px-sm-3 mx-6 mb-2 text-noir ">
                    <li>
                        Contexte : La pression réglementaire et la demande des consommateurs pour des produits plus respectueux de l’environnement.    
                    </li>
                    <section class="py-1"></section>
                    <li>
                        Exemple de mission : Développer des centres de données à faible consommation énergétique ou des systèmes de production d’énergie renouvelable.
                    </li>
                </ul>
            </div>
            <div>
                <section class="py-3"></section>
                <div
                        class="d-flex justify-content-between align-items-center mb-2"
                    >
                        <h3 class="mb-0 text-noir ">B. Consultant en Green IT</h3>
                </div>
                <p class="text-lg mb-0 py-2 text-noir ">
                    Le consultant en Green IT aide les entreprises à réduire l’empreinte carbone de leurs infrastructures informatiques.
                    <br />
                </p>
                <section class="py-1"></section>
                <ul class="custom-list col-lg-11 col-md-9 z-index-2 position-relative px-md-0 px-sm-3 mx-6 mb-2 text-noir ">
                    <li>
                        Croissance attendue : La demande pour ce métier pourrait augmenter de +25 % d’ici 2025, selon Forbes. 
                    </li>
                    <section class="py-1"></section>
                    <li>
                        Impact : Optimisation de la consommation énergétique des data centers, promotion de pratiques durables dans le cycle de vie des équipements IT.    
                    </li>

                </ul>
            </div>
 
 
        </div>

        <div class="quote-box">
                <p class="quote-text text-noir ">
                        “Les métiers tech de 2025 seront façonnés par l’évolution rapide des technologies et les nouvelles exigences du marché. Intelligence artificielle, cybersécurité, data et technologies vertes : ces secteurs sont en pleine effervescence. ”
                </p>
        </div>


            </div>
          </div>
        </div>
      </div>
    </div>
    </section>

    <section class="py-5"></section>
  </div>
  <DefaultFooter />
</template>

<style scoped>
.quote-box {
  border-left: 3px solid #e16e22; /* Bordure gauche colorée */
  background-color: #e6e8ed;     /* Couleur de fond */
  padding: 20px;                 /* Espacement interne */
  border-radius: 8px;            /* Coins arrondis */
  font-style: italic;            /* Texte en italique */
  color: #6b6b6b;                /* Couleur du texte */
  line-height: 1.5;              /* Espacement des lignes */
  margin-top: 20px;              /* Espacement au-dessus */
}

.quote-text {
  margin: 0; /* Supprime les marges par défaut */
}
.text-noir {
  color: #333333; /* Noir */
}
</style>
