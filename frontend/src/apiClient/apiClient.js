// apiClient.js
import axios from "axios";

import { api_base_url } from '../settings/settings'

const apiClient = axios.create({
  baseURL: api_base_url,
  timeout: 8000,
  headers: {
    "Content-Type": "application/json",
  },
});

export default apiClient;
