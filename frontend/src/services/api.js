import axios from 'axios';

const api = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

export const polygonAPI = {
  getAll: async () => {
    const response = await api.get('/polygons/');
    return response.data;
  },

  getById: async (id) => {
    const response = await api.get(`/polygons/${id}/`);
    return response.data;
  },

  create: async (polygonData) => {
    const response = await api.post('/polygons/', polygonData);
    return response.data;
  },

  update: async (id, polygonData) => {
    const response = await api.put(`/polygons/${id}/`, polygonData);
    return response.data;
  },

  delete: async (id) => {
    const response = await api.delete(`/polygons/${id}/`);
    return response.data;
  },

  getGeoJSON: async (id) => {
    const response = await api.get(`/polygons/${id}/geojson/`);
    return response.data;
  },

  getGeoJSONCollection: async () => {
    const response = await api.get('/polygons/geojson_collection/');
    return response.data;
  },
};

export default api; 