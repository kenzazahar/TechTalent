<template>
    <div class="application-form">
      <h1 class="form-title">Postuler - {{ offer?.title }}</h1>
      
      <form @submit.prevent="handleSubmit" class="form-content">
        <div class="form-group">
          <label for="firstName">Prénom <span class="required">*</span></label>
          <input
            id="firstName"
            v-model="formData.firstName"
            type="text"
            required
            class="form-input"
          />
        </div>
  
        <div class="form-group">
          <label for="lastName">Nom <span class="required">*</span></label>
          <input
            id="lastName"
            v-model="formData.lastName"
            type="text"
            required
            class="form-input"
          />
        </div>
  
        <div class="form-group">
          <label for="email">Email <span class="required">*</span></label>
          <input
            id="email"
            v-model="formData.email"
            type="email"
            required
            class="form-input"
          />
        </div>
  
        <div class="form-group">
          <label for="phone">Téléphone</label>
          <input
            id="phone"
            v-model="formData.phone"
            type="tel"
            class="form-input"
          />
        </div>
  
        <div class="form-group">
          <label for="cv">CV <span class="required">*</span></label>
          <input
            id="cv"
            type="file"
            @change="handleFileUpload('cv', $event)"
            accept=".pdf,.doc,.docx"
            required
            class="form-input"
          />
        </div>
  
        <div class="form-group">
          <label for="coverLetter">Lettre de motivation</label>
          <input
            id="coverLetter"
            type="file"
            @change="handleFileUpload('coverLetter', $event)"
            accept=".pdf,.doc,.docx"
            class="form-input"
          />
        </div>
  
        <div class="form-group">
          <label for="message">Message complémentaire</label>
          <textarea
            id="message"
            v-model="formData.message"
            rows="4"
            class="form-input"
          ></textarea>
        </div>
  
        <p class="required-notice">Les champs marqués d'un astérisque (*) sont obligatoires.</p>
  
        <div class="action-buttons">
          <button type="button" @click="handleCancel" class="btn-cancel">
            Annuler
          </button>
          <button type="submit" class="btn-submit">
            Envoyer ma candidature
          </button>
        </div>
      </form>
    </div>
    <DefaultFooter />
  </template>
  
  <script setup>
  import { ref, defineProps } from 'vue';
  import { useRouter } from 'vue-router';
  import DefaultFooter from "./footers/FooterDefault.vue";
  
  const props = defineProps({
    offer: {
      type: Object,
      required: true
    }
  });
  
  const router = useRouter();
  
  const formData = ref({
    firstName: '',
    lastName: '',
    email: '',
    phone: '',
    cv: null,
    coverLetter: null,
    message: ''
  });
  
  const handleFileUpload = (type, event) => {
    const file = event.target.files[0];
    if (file) {
      formData.value[type] = file;
    }
  };
  
  const handleSubmit = async () => {
    try {
      // Ici, ajoutez la logique pour envoyer les données du formulaire
      console.log('Données du formulaire:', formData.value);
      
      // Redirection vers le dashboard après soumission réussie
      router.push('/candidate/dashboard');
    } catch (error) {
      console.error('Erreur lors de l\'envoi de la candidature:', error);
    }
  };
  
  const handleCancel = () => {
    router.push('/candidate/dashboard');
  };
  </script>
  
  <style scoped>
  .application-form {
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem;
    background: white;
    border-radius: 0.5rem;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    font-family: system-ui, -apple-system, sans-serif;
  }
  
  .form-title {
    font-size: 1.75rem;
    font-weight: 700;
    color: #1a1a1a;
    margin-bottom: 2.5rem;
    text-align: center;
    letter-spacing: -0.025em;
  }
  
  .form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 600;
    color: #374151;
    font-size: 0.95rem;
    letter-spacing: 0.025em;
  }
  
  /* Style personnalisé pour les boutons d'import de fichiers */
  .form-input[type="file"] {
    display: none;
  }
  
  .form-group:has(input[type="file"]) label {
    display: inline-block;
    cursor: pointer;
    background-color: #f8f9fa;
    padding: 0.75rem 1rem;
    border: 2px dashed #e2e8f0;
    border-radius: 0.5rem;
    width: 100%;
    text-align: center;
    transition: all 0.2s ease;
  }
  
  .form-group:has(input[type="file"]) label:hover {
    background-color: #edf2f7;
    border-color: #cbd5e1;
  }
  
  .form-group:has(input[type="file"]) label::before {
    content: "📎 Cliquez pour ajouter un fichier";
    color: #4a5568;
    font-weight: 500;
  }
  
  /* Style des autres champs */
  .form-input {
    width: 100%;
    padding: 0.75rem;
    border: 1.5px solid #E5E7EB;
    border-radius: 0.5rem;
    font-size: 1rem;
    transition: all 0.2s ease;
    color: #1a1a1a;
    background-color: #fff;
  }
  
  .form-input:focus {
    outline: none;
    border-color: #1d1d21;
    box-shadow: 0 0 0 3px rgba(29, 29, 33, 0.1);
  }
  
  /* Style du textarea */
  textarea.form-input {
    resize: vertical;
    min-height: 120px;
    line-height: 1.5;
  }
  
  /* Textes informatifs */
  .required {
    color: #DC2626;
    margin-left: 0.25rem;
    font-weight: bold;
  }
  
  .required-notice {
    font-size: 0.875rem;
    color: #6B7280;
    margin-bottom: 2rem;
    font-style: italic;
  }
  
  /* Boutons d'action */
  .action-buttons {
    display: flex;
    gap: 1rem;
    justify-content: flex-end;
    margin-top: 2.5rem;
  }
  
  .btn-submit, .btn-cancel {
    padding: 0.75rem 2rem;
    border-radius: 0.5rem;
    font-weight: 600;
    transition: all 0.2s ease;
    text-transform: uppercase;
    letter-spacing: 0.025em;
    font-size: 0.875rem;
  }
  
  .btn-submit {
    background-color: #1d1d21;
    color: white;
    border: none;
  }
  
  .btn-submit:hover {
    background-color: #000000;
    transform: translateY(-1px);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .btn-cancel {
    background-color: #F3F4F6;
    color: #4B5563;
    border: 1px solid #E5E7EB;
  }
  
  .btn-cancel:hover {
    background-color: #E5E7EB;
    color: #1F2937;
  }
  </style>