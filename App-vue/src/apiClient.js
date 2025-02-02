import axios from 'axios';

const API_URL = 'http://localhost:8000';

// Fonction pour obtenir le cookie CSRF
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

const apiClient = axios.create({
  baseURL: API_URL,
  withCredentials: true // Important pour les cookies CSRF
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
    // Log pour débugger
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

export const loginUser = async (credentials) => {
  try {
    const response = await apiClient.post('/api/login/', credentials);
    return response.data;
  } catch (error) {
    throw error.response ? error.response.data : error;
  }
};

export default apiClient;