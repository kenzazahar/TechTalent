<script setup>
import { onMounted, onUnmounted } from "vue";

//example components
import DefaultNavbar from "./navbars/NavbarDefaults.vue";
import DefaultFooter from "./footers/FooterDefault.vue";

//dep
import Typed from "typed.js";

//images
import bg0 from "@/assets/img/bg92.jpg";


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
                Emploi entretien d'embauche 
            </h1>
            <p class="lead mb-4 text-white opacity-8">
                Le but du recruteur n’est pas de vous piéger mais de vous inciter à parler de vous pour le convaincre que vous êtes le meilleur candidat.
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
              class="col-lg-10 col-md-7 z-index-2 position-relative px-md-2 px-sm-5 mx-8 text-dark"
            >

        <div>
              <div
                class="d-flex justify-content-between align-items-center mb-2 py-2"
              >
                <h5 class="mb-0 text-noir ">Emploi entretien d'embauche</h5>
              </div>
              <div
                class="d-flex justify-content-between align-items-center mb-2 py-2"
              >
                <h1 class="mb-0 text-noir ">Conseils pour bien préparer votre entretien d'embauche</h1>
              </div>
              <p class="text-lg mb-0 py-1 text-noir ">
                Un entretien d'embauche est un processus par lequel un employeur évalue les compétences
                 et les qualifications d'un candidat pour un poste vacants. Il peut être mené en personne, 
                 par téléphone ou par vidéoconférence. Lors de l'entretien, l'employeur posera des questions 
                 sur le parcours professionnel et les compétences du candidat, ainsi que sur ses motivations 
                 et ses aspirations professionnelles. Le but de l'entretien est de déterminer si le candidat 
                 est qualifié pour le poste et s'il s'intégrera bien à l'équipe et à la culture de l'entreprise.
                <br />
              </p>
              <p class="text-lg mb-0 py-1 text-noir ">
                Il est important de se préparer à l'entretien en étudiant les informations sur l'entreprise et 
                le poste, en réfléchissant aux réponses aux questions courantes, et en préparant des exemples 
                de situations professionnelles que vous avez vécues et les résultats que vous avez obtenus.
                <br />
              </p>
              
              <div class="quote-box">
                <p class="quote-text text-noir ">
                        “L'entretien d'embauche est comme une danse de ballet. Le candidat doit être précis,
                        fluide et gracieux dans ses réponses, tandis que l'employeur doit être attentif, professionnel 
                        et critique dans ses questions. Ensemble, ils doivent créer une performance harmonieuse pour 
                        arriver à un résultat commun : un emploi pour le candidat et un employé qualifié pour l'entreprise.”
                </p>
             </div>
        </div>

        <div>
            <section class="py-4"></section>
            <div
                    class="d-flex justify-content-between align-items-center mb-2"
                >
                    <h2 class="mb-0 text-noir ">Avant l'entretien d'embauche : ce qu’il faut faire pour le réussir</h2>
            </div>

            <p class="text-lg mb-0 py-2 text-noir ">
                    Pour réussir, mieux vaut bien se préparer à l'entretien d’embauche en amont afin de ne pas vous faire piéger par les questions du recruteur. Voici quelques conseils à suivre avant votre entretien.
                <br />
            </p>
            <div>
                <section class="py-3"></section>
                <div
                        class="d-flex justify-content-between align-items-center mb-2"
                    >
                        <h3 class="mb-0 text-noir ">1. Faire des recherches sur l’entreprise</h3>
                </div>
                <p class="text-lg mb-0 py-2 text-noir ">
                    Pour préparer votre entretien d'embauche, vous pouvez faire des recherches :
                    <br />
                </p>
                <section class="py-1"></section>
                <ul class="custom-list col-lg-11 col-md-9 z-index-2 position-relative px-md-0 px-sm-3 mx-6 mb-2 text-noir ">
                    <li>
                    Faire des recherches sur l’entreprise que vous souhaitez intégrer. Renseignez-vous sur son histoire, sa direction et 
                    ses principales réussites, ses valeurs et sa culture d’entreprise.
                    </li>
                    <section class="py-1"></section>
                    <li>
                    Chercher des informations sur la personne que vous allez rencontrer lors de votre entretien : essayez de trouver quel
                    est son rôle au sein de l’entreprise. Est-elle membre des ressources humaines ou bien manager de l’équipe que vous êtes en passe d’intégrer ?
                    </li>
                </ul>
                <p class="text-lg mb-0 py-2 text-noir">
                    Continuez vos recherches en relisant précisément l’annonce à laquelle vous avez répondu. Vous y trouverez de nombreux 
                    indices sur ce que recherche le recruteur, comme les compétences de la candidate ou du candidat idéal. Essayez aussi d’identifier 
                    vos points forts et vos points faibles.
                    <br />
                </p>
                <p class="text-lg mb-0 py-2 text-noir ">
                    Le recruteur doit sentir que vous avez travaillé et effectué des recherches avant de participer à une entrevue : une forme de
                    politesse autant qu’un signe de motivation. Il est d’ailleurs possible que le recruteur vous demande directement après la
                    présentation de votre parcours : que savez-vous de nous ? Qu’avez-vous compris de notre métier ?
                    <br />
                </p>
            </div>
            <div>
                <section class="py-3"></section>
                <div
                        class="d-flex justify-content-between align-items-center mb-2"
                    >
                        <h3 class="mb-0 text-noir ">2. S’entraîner à répondre aux questions</h3>
                </div>
                <p class="text-lg mb-0 py-2 text-noir ">
                    Certaines questions reviennent systématiquement lors des entretiens d'embauche. Il peut être intéressant pour vous de préparer
                     vos réponses. Le recruteur pourrait par exemple vous demander :
                    <br />
                </p>
                <section class="py-1"></section>
                <ul class="custom-list col-lg-11 col-md-9 z-index-2 position-relative px-md-0 px-sm-3 mx-6 mb-2 text-noir ">
                    <li>
                        Pourquoi souhaitez-vous travailler dans cette entreprise ?
                    </li>
                   
                    <li>
                        Parlez-moi de vous.
                    </li>
                    
                    <li>
                        Quels sont vos points forts et vos points faibles ?
                    </li>
                </ul>
                <div class="quote-box">
                    <p class="quote-text text-noir ">
                            “« Quelle est votre plus grande force ? » est une question très directe que vous avez de grandes chances de croiser lors de vos entretiens. Si elle peut sembler
                            l’une des plus simples, elle peut vous conduire à faire quelques faux pas si vous ne l’avez pas préparée à l’avance. De plus, donner une réponse de qualité qui évite les 
                            clichés n’est pas toujours  facile. ”
                    </p>
                </div>

                <section class="py-2"></section>
                <p class="text-lg mb-0 py-2 text-noir ">
                    Dans certains cas, les recruteurs et recruteuses posent également des questions de mise en situation qui lui permettent de tester 
                    la manière de réagir des futurs candidats et candidates dans l’exercice de leur profession. Pour y répondre, vous pouvez utiliser
                     une méthode en trois temps :
                    <br />
                </p>
                <section class="py-1"></section>
                <ul class="custom-list col-lg-11 col-md-9 z-index-2 position-relative px-md-0 px-sm-3 mx-6 mb-2 text-noir ">
                    <li>
                        commencez par détailler la situation ;
                    </li>
                    
                    <li>
                        expliquez ensuite la solution que vous mettriez en place,
                    </li>
                    
                    <li>
                        puis terminez en expliquant les bénéfices que l’employeur tirera de vos actions après avoir résolu le problème.
                    </li>
                </ul>
                <p class="text-lg mb-0 py-2 text-noir ">
                    Pour plus de réalisme, vous pouvez demander à des membres de votre famille ou de votre cercle amical de vous faire répéter quelques 
                    jours avant votre entretien. Vous pourrez alors vous entraîner à répondre aux questions et définir les points sur lesquels vous pouvez encore vous améliorer.
                    <br />
                </p>
                <p class="text-lg mb-0 py-2 text-noir ">
                    N'oubliez pas non plus que certaines questions sont interdites en entretien et que vous n'avez aucune obligation d'y répondre.
                    <br />
                </p>
            </div>
            <div>
                <section class="py-3"></section>
                <div
                        class="d-flex justify-content-between align-items-center mb-2"
                    >
                        <h3 class="mb-0 text-noir ">3. Se préparer à parler de la rémunération</h3>
                </div>
                <p class="text-lg mb-0 py-2 text-noir ">
                    Il est parfois difficile d’aborder le sujet du salaire pendant un entretien d'embauche, surtout sans vous y préparer. Le recruteur pourrait cependant vous demander vos prétentions salariales s’il décidait de vous accorder le poste.
                    <br />
                </p>
                <p class="text-lg mb-0 py-2 text-noir ">
                    Prenez donc le temps de les définir. Les négociations de salaire se font habituellement en salaire brut et non en net. Pour préparer cette question, posez-vous ces questions :
                    <br />
                </p>
                <section class="py-1"></section>
                <ul class="custom-list col-lg-11 col-md-9 z-index-2 position-relative px-md-0 px-sm-3 mx-6 mb-2 text-noir ">
                    <li>
                        Quels sont les montants moyens des salaires pratiqués à poste équivalent dans le secteur ? Il s’agit ici de ne pas être en complet décalage avec ce que vous allez demander par la suite.
                    </li>
                    <section class="py-1"></section>
                    <li>
                        Quel est le montant annuel brut que vous souhaitez obtenir ?
                    </li>
                    <section class="py-1"></section>
                    <li>
                        Quel est le montant mensuel brut que vous aimeriez obtenir ?
                    </li>
                </ul>
                <p class="text-lg mb-0 py-2 text-noir ">
                    Mémorisez les montants afin de pouvoir les énoncer au recruteur lors de l’entretien.
                    <br />
                </p>
            </div>
            <div>
                <section class="py-3"></section>
                <div
                        class="d-flex justify-content-between align-items-center mb-2"
                    >
                        <h3 class="mb-0 text-noir ">4. Choisir sa tenue vestimentaire</h3>
                </div>
                <p class="text-lg mb-0 py-2 text-noir ">
                    La tenue que vous porterez le jour de votre entretien est un élément essentiel de votre réussite à venir. Elle doit refléter votre professionnalisme, mais aussi être en adéquation avec la culture de l’entreprise. 
                    Choisissez-la à l’avance et vérifiez qu’elle n’est pas froissée ni n’a de tâche.
                    <br />
                </p>
                <p class="text-lg mb-0 py-2 text-noir ">
                    Dans tous les cas, veillez à ce qu’elle soit confortable. Vous n’aurez ainsi pas de mauvaise surprise le matin de votre entretien d’embauche.
                    <br />
                </p>
            </div>
            <div>
                <section class="py-3"></section>
                <div
                        class="d-flex justify-content-between align-items-center mb-2"
                    >
                        <h3 class="mb-0 text-noir ">5. Se relaxer</h3>
                </div>
                <p class="text-lg mb-0 py-2 text-noir ">
                    Pour éviter un stress trop important le jour de votre entretien d’embauche, il est essentiel de vous relaxer un maximum avant le jour J :
                    <br />
                </p>
                <section class="py-1"></section>
                <ul class="custom-list col-lg-11 col-md-9 z-index-2 position-relative px-md-0 px-sm-3 mx-6 mb-2 text-noir ">
                    <li>
                        Évitez de faire vos recherches au dernier moment et passez plutôt votre soirée à vous détendre.   
                    </li>
                    <section class="py-1"></section>
                    <li>
                        
                        Vous pouvez également faire quelques exercices de méditation ou de respiration qui vous aideront à canaliser votre stress.
                    </li>
                    <section class="py-1"></section>
                    <li>
                        Mangez sainement, et veillez à dormir suffisamment afin d’être en pleine forme.
                    </li>
                </ul>                
            </div>
 
        </div>

        <div>
            <section class="py-4"></section>
            <div
                    class="d-flex justify-content-between align-items-center mb-2"
                >
                    <h2 class="mb-0 text-noir ">Pendant son entretien d’embauche : ce qu’il faut faire pour le réussir</h2>
            </div>

            <p class="text-lg mb-0 py-2 text-noir ">
                Le jour J est arrivé. Maintenant que votre préparation est faite, il est temps de passer à l’action et de réussir votre entretien d’embauche.
                <br />
            </p>
            <div>
                <section class="py-2"></section>
                <div
                        class="d-flex justify-content-between align-items-center mb-2"
                    >
                        <h3 class="mb-0 text-noir ">6. Arriver en avance </h3>
                </div>
                <p class="text-lg mb-0 py-2 text-noir ">
                    Quelle que soit la durée de votre entretien d'embauche, la première impression est extrêmement importante.
                    <br />
                </p>
                <p class="text-lg mb-0 py-2 text-noir ">
                    Pas question donc d’avoir du retard à votre entretien : vous passeriez immédiatement pour une personne manquant de professionnalisme et peu fiable auprès du recruteur. Dans l’idéal :
                    <br />
                </p>
                <section class="py-1"></section>
                <ul class="custom-list col-lg-11 col-md-9 z-index-2 position-relative px-md-0 px-sm-3 mx-6 mb-2 text-noir ">
                    <li>
                        Étudiez votre trajet la veille de votre entretien et estimez le temps nécessaire pour vous rendre sur place, mais aussi pour vous garer si vous vous y rendez en voiture.
                    </li>
                    <section class="py-1"></section>
                    <li>
                        Gardez toujours une marge confortable afin d’arriver à l’heure. Vous pourriez alors vous laisser déstabiliser par le stress provoqué par cette situation.
                    </li>
                    <section class="py-1"></section>
                    <li>
                        Si vous prenez les transports en commun pour vous rendre sur le lieu de l’entretien, prévoyez une solution de repli si des problèmes devaient survenir pendant le trajet.
                    </li>
                </ul>
                <p class="text-lg mb-0 py-2 text-noir ">
                    Vous passez un entretien Skype ? À la bonne heure ! Vous n'aurez pas à vous inquiéter du temps de trajet. Toutefois, n'en négligez pas la ponctualité pour autant et préparez votre entretien avec autant de sérieux que vous le feriez en présentiel. Connectez-vous quelques minutes en avance, notamment pour préparer 'arrière-plan de votre réunion et soigner le cadre pour cette première impression.
                    <br />
                </p>
                
            </div>
            <div>
                <div class="quote-box">
                <p class="quote-text text-noir ">
                    Éteindre son téléphone portable
                    Il serait malvenu que votre smartphone se mette à sonner frénétiquement durant votre entretien. Éteignez-le complètement lorsque vous arrivez dans la salle d’attente ou mettez-le en mode silencieux, tout en prenant soin de retirer le vibreur. Contrairement à ce que l’on pourrait croire, cela peut également être bruyant.       
                </p>
             </div>
                
            </div>
            <div>
                <section class="py-4"></section>
                <div
                        class="d-flex justify-content-between align-items-center mb-2"
                    >
                        <h3 class="mb-0 text-noir ">7. Prendre le temps de répondre aux questions</h3>
                </div>
                <p class="text-lg mb-0 py-2 text-noir ">
                    Même si vous avez très certainement envie de montrer toute votre motivation au recruteur, rien ne sert de se presser. Prenez d’abord le temps de bien étudier ses questions afin de ne pas répondre à côté. Dans votre tête, listez ensuite les arguments les plus importants, puis formulez des réponses courtes et claires. N’hésitez pas à donner des exemples précis de vos réussites précédentes.
                    <br />
                </p>
                
            </div>           
            <div>
                <section class="py-3"></section>
                <div
                        class="d-flex justify-content-between align-items-center mb-2"
                    >
                        <h3 class="mb-0 text-noir ">8. Poser des questions au recruteur</h3>
                </div>
                <p class="text-lg mb-0 py-2 text-noir ">
                    À la fin de votre entretien d'embauche, le recruteur vous demandera certainement si vous avez des questions à lui poser ou des précisions à lui demander sur le poste à pourvoir. Pour montrer votre intérêt, il peut être intéressant d’en avoir préparé quelques-unes.
                    <br />
                </p>
                <p class="text-lg mb-0 py-2 text-noir ">
                    Voici quelques exemples de questions à poser en fin d’entretien. N’hésitez pas à les personnaliser en fonction du poste que vous convoitez.
                    <br />
                </p>
                <section class="py-1"></section>
                <ul class="custom-list col-lg-11 col-md-9 z-index-2 position-relative px-md-0 px-sm-3 mx-6 mb-2 text-noir ">
                    <li>
                        Sur quels types de projets travaillez-vous en ce moment ?    
                    </li>
                    <section class="py-1"></section>
                    <li>
                        Comment fonctionne votre équipe ? De combien de membres est-elle constituée ?
                    </li>
                    <section class="py-1"></section>
                    <li>
                        Quelles sont les perspectives d’évolution pour ce poste ?
                    </li>
                    <section class="py-1"></section>
                    <li>
                        Comment les performances sont-elles évaluées pour ce poste ?    
                    </li>
                </ul>
            </div>
            <div>
                <section class="py-3"></section>
                <div
                        class="d-flex justify-content-between align-items-center mb-2"
                    >
                        <h3 class="mb-0 text-noir ">9. Prêter attention à son langage corporel</h3>
                </div>
                <p class="text-lg mb-0 py-2 text-noir ">
                    La manière dont vous allez vous comporter durant votre entretien d’embauche est tout aussi importante que ce que vous allez dire au recruteur. Grâce à votre langage corporel, vous pourrez renforcer l’impression positive que vous lui laisserez.
                    <br />
                </p>
                <p class="text-lg mb-0 py-2 text-noir ">
                    Commencez par une poignée de main ferme, avec une intensité raisonnable lorsque vous vous le saluez. Durant l’entretien, prêtez attention à votre posture : gardez le dos et le menton droit. Regardez également le recruteur dans les yeux, et n’hésitez pas à hocher la tête pour signaler votre approbation. Afficher un léger sourire montrera que vous êtes une personne positive et motivée.
                    <br />
                </p>
            </div> 
        </div>

        <div>
            <section class="py-4"></section>
            <div
                    class="d-flex justify-content-between align-items-center mb-2"
                >
                    <h2 class="mb-0 text-noir ">Après l'entretien d’embauche : ce qu’il faut faire pour le réussir</h2>
            </div>

            <p class="text-lg mb-0 py-2 text-noir ">
                Votre entretien ne se termine pas une fois la porte de l’entreprise franchie. Il reste encore quelques étapes afin de mettre toutes les chances de votre côté pour réussir votre entretien d’embauche.
                <br />
            </p>
            <div>
                <section class="py-2"></section>
                <div
                        class="d-flex justify-content-between align-items-center mb-2"
                    >
                        <h3 class="mb-0 text-noir ">10. Envoyer un mail de remerciement</h3>
                </div>
                <p class="text-lg mb-0 py-2 text-noir ">
                    Deux ou trois jours après votre entretien, envoyez un email de remerciement au recruteur rencontré. Vous lui remémorerez ainsi votre candidature et lui montrerez votre motivation pour le poste visé. Vous lui témoignerez aussi que vous avez bien compris ses attentes.
                    <br />
                </p>
                <p class="text-lg mb-0 py-2 text-noir ">
                    Ce courriel de remerciement doit être court. Dans un premier temps, commencez par rappeler au recruteur la date à laquelle a eu lieu votre entretien d'embauche. Réitérez ensuite votre motivation pour obtenir le poste, tout en vous appuyant sur un point abordé lors de votre rencontre. Il ne s’agit pas ici de reproduire votre lettre de motivation. Terminez simplement avec une formule de politesse.
                    <br />
                </p>
            </div>
           
            <div>
                <section class="py-3"></section>
                <div
                        class="d-flex justify-content-between align-items-center mb-2"
                    >
                        <h3 class="mb-0 text-noir ">11. Relancer le recruteur ou la recruteuse</h3>
                </div>
                <p class="text-lg mb-0 py-2 text-noir ">
                    En général, le recruteur vous donnera la date approximative à laquelle il vous recontactera afin de vous faire part de sa réponse. Mais il peut arriver que la prise de décision soit plus longue. Sans nouvelle de sa part plusieurs jours après la date prévue, vous pouvez le relancer par courriel afin de savoir si une décision a été prise concernant le poste à pourvoir. Vous pouvez également l’appeler pour obtenir une réponse et savoir s’il compte donner suite à votre entretien.
                    <br />
                </p>
                
            </div>           
        </div>

        <div class="quote-box">
                <p class="quote-text text-noir ">
                        “Vous savez désormais comment mettre toutes les chances de votre côté pour réussir un entretien d'embauche. Préparez-vous minutieusement, faites bonne impression le jour J et n'hésitez pas à recontacter le recruteur après l'entretien. Nous espérons que ces conseils vous aideront à obtenir le poste que vous convoitez : bon courage !”
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

