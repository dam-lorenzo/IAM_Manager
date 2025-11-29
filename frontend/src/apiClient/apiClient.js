// apiClient.js
import axios from "axios";

const apiClient = axios.create({
  baseURL: process.env.REACT_APP_API_URL,
  timeout: 8000,
  headers: {
    "Content-Type": "application/json",
  },
});

export default apiClient;
