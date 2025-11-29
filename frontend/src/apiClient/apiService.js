import apiClient from "./apiClient";

// Delay async
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

const shouldRetry = (error) => {
  // Reintentar solo si:
  // - NO hubo respuesta del servidor (timeout / pérdida de conexión)
  // - SÍ hubo request enviado
    return error.request && !error.response;
};

export const apiGet = async (url, params = {}) => {
    try {
        const { data } = await apiClient.get(url, { params });
        return data;
    } catch (error) {
        console.error("GET error:", error);
        throw error;
    }
};

export const apiPost = async (url, body, { retries = 3, delay = 1000 } = {}) => {
    for (let attempt = 1; attempt <= retries; attempt++) {
        try {
            const { data } = await apiClient.post(url, body);
            return data;
        } catch (error) {
            if (!shouldRetry(error) || attempt === retries) throw error;
            await sleep(delay);
        }
    }
};

export const apiPut = async (url, body, { retries = 3, delay = 1000 } = {}) => {
    for (let attempt = 1; attempt <= retries; attempt++) {
        try {
            const { data } = await apiClient.put(url, body);
            return data;
        } catch (error) {
            if (!shouldRetry(error) || attempt === retries) throw error;
            await sleep(delay);
        }
    }
};

/* ------------------------------ DELETE ------------------------------ */
export const apiDelete = async (url) => {
    try {
        const { data } = await apiClient.delete(url);
        return data;
    } catch (error) {
        console.error("DELETE error:", error);
        throw error;
    }
};

apiPut(url, body, {  })
