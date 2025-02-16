import axios from 'axios';

const API_URL = 'http://localhost:8000';

// Fonction pour obtenir le cookie CSRF
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

const apiClient = axios.create({
  baseURL: 'http://localhost:8000',
  withCredentials: true, // Important pour les cookies CSRF
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${localStorage.getItem('token')}`
  }
});

// Intercepteur pour ajouter le token CSRF à chaque requête
apiClient.interceptors.request.use(
  config => {
    // Obtenir le token CSRF du cookie
    const csrfToken = getCookie('csrftoken');
    if (csrfToken) {
      config.headers['X-CSRFToken'] = csrfToken;
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

export const registerStudent = async (formData) => {
  try {
    console.log('Sending registration data:', formData);
    
    const response = await apiClient.post('/api/register/student/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    console.log('Registration response:', response);
    return response.data;
  } catch (error) {
    console.error('Registration error:', error);
    if (error.response) {
      console.error('Error response:', error.response.data);
    }
    throw error.response ? error.response.data : error;
  }
};

export const registerCompany = async (formData) => {
  try {
    console.log('Sending company registration data:', formData);
    
    const response = await apiClient.post('/api/register/company/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    console.log('Company registration response:', response);
    return response.data;
  } catch (error) {
    console.error('Company registration error:', error);
    if (error.response) {
      console.error('Error response:', error.response.data);
    }
    throw error.response ? error.response.data : error;
  }
};

export const loginUser = async (credentials) => {
  try {
    const response = await apiClient.post('/api/login/', credentials);
    return response.data;
  } catch (error) {
    throw error.response ? error.response.data : error;
  }
};


export const getProfile = async () => {
  try {
    console.log('Fetching profile...');
    const response = await apiClient.get('/api/profile/');
    console.log('Profile response:', response.data);
    return response.data;
  } catch (error) {
    console.error('Profile fetch error:', error);
    if (error.response) {
      console.error('Error response:', error.response.data);
      throw new Error(error.response.data.error || 'Erreur serveur');
    }
    throw error;
  }
};


export const updateProfile = async (formData) => {
  try {
    const response = await apiClient.post('/api/profile/update/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  } catch (error) {
    console.error("Erreur lors de la mise à jour du profil :", error.response?.data || error.message);
    throw new Error(error.response?.data?.message || "Échec de la mise à jour du profil.");
  }
};


export const getCompanyProfile = async () => {
  try {
    const response = await apiClient.get('/api/company/profile/');
    console.log('Company profile response:', response.data); // Debug
    return response.data;
  } catch (error) {
    console.error('Company profile fetch error:', error);
    throw error;
  }
};

export const updateProfilecompany = async (formData) => {
  try {
    const response = await apiClient.post('/api/company/profile/update/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  } catch (error) {
    console.error("Erreur lors de la mise à jour du profil :", error.response?.data || error.message);
    throw new Error(error.response?.data?.message || "Échec de la mise à jour du profil.");
  }
};


export const createJobOffer = async (formData, isPublish = true) => {
  try {
    const form = new FormData();
    Object.keys(formData).forEach(key => {
      if (formData[key] !== null) {
        form.append(key, formData[key]);
      }
    });
    
    // Convertir explicitement en string 'true' ou 'false'
    form.append('isPublish', String(isPublish));

    const response = await apiClient.post('/api/job-offers/create/', form, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  } catch (error) {
    console.error('Error creating job offer:', error);
    throw error.response ? error.response.data : error;
  }
};

// Get published offers
export const getPublishedOffers = async () => {
  try {
    const response = await apiClient.get('/api/job-offers/published/');
    return response.data;
  } catch (error) {
    console.error('Error fetching published offers:', error);
    throw error;
  }
};

// Get draft offers
export const getDraftOffers = async () => {
  try {
    const response = await apiClient.get('/api/job-offers/drafts/');
    return response.data;
  } catch (error) {
    console.error('Error fetching draft offers:', error);
    throw error;
  }
};


export const updateJobOffer = async (id, formData) => {
  try {
    const response = await apiClient.patch(`/api/job-offers/${id}/update/`, formData, {
      headers: {
        'Content-Type': 'application/json',
      },
    });
    return response.data;
  } catch (error) {
    console.error('Error updating job offer:', error);
    throw error.response ? error.response.data : error;
  }
};

// Fonction pour supprimer une offre
export const deleteJobOffer = async (id) => {
  try {
    const response = await apiClient.delete(`/api/job-offers/${id}/`);
    return response.data;
  } catch (error) {
    console.error('Error deleting job offer:', error);
    throw error.response ? error.response.data : error;
  }
};

export const getAllPublishedOffers = async () => {
  try {
    const response = await apiClient.get('/api/job-offers/all-published/');
    return response.data;
  } catch (error) {
    if (error.response) {
      // Le serveur a répondu avec un statut d'erreur
      console.error('Server error:', error.response.data);
    } else if (error.request) {
      // La requête a été faite mais pas de réponse reçue
      console.error('No response received:', error.request);
    } else {
      // Une erreur s'est produite lors de la configuration de la requête
      console.error('Error setting up request:', error.message);
    }
    throw error;
  }
};

export const createApplication = async (formData) => {
  try {
    const response = await apiClient.post('/applications/create/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
      withCredentials: true, // 🔹 Ajoute ceci pour s'assurer que les cookies d'auth sont envoyés
    });
    return response.data;
  } catch (error) {
    console.error('Erreur API (createApplication) :', error.response?.data || error);
    throw error.response ? error.response.data : error;
  }
};


export const getCompanyApplications = async (offerId) => {
  try {
    const response = await apiClient.get(`/applications/company/${offerId}/`);
    return response.data;
  } catch (error) {
    console.error('Erreur lors de la récupération des candidatures pour l\'offre :', error);
    throw error.response ? error.response.data : error;
  }
};

export const updateApplicationStatus = async (applicationId, status) => {
  try {
    const response = await apiClient.patch(`/applications/update-status/${applicationId}/`, { status });
    return response.data;
  } catch (error) {
    console.error('Erreur lors de la mise à jour du statut de la candidature :', error);
    throw error.response ? error.response.data : error;
  }
};

export const getStudentApplications = async () => {
  try {
    console.log('Fetching student applications...');
    const response = await apiClient.get('/applications/student/');
    console.log('Response received:', response.data);
    return response.data;
  } catch (error) {
    console.error('API error details:', error.response?.data);
    throw error;
  }
};

export const deleteApplication = async (applicationId) => {
  try {
    const response = await apiClient.delete(`/applications/${applicationId}/`)
    return response.data
  } catch (error) {
    console.error('Erreur API (deleteApplication) :', error.response?.data || error)
    throw error.response ? error.response.data : error
  }
}


export default apiClient;