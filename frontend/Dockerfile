# Usar Node.js como base
FROM node:20-alpine

# Crear carpeta de trabajo
WORKDIR /app

# Copiar package.json y package-lock.json
COPY package*.json ./

# Instalar dependencias
RUN npm install

# Copiar todo el proyecto
COPY . .

# Exponer el puerto que usa React por defecto
EXPOSE 5173

# Comando para levantar la app en modo desarrollo
CMD ["npm", "start"]
