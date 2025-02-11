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

export default apiClient;