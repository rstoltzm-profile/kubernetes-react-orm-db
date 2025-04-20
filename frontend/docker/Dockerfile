# Use Node.js 18 as the base image
FROM node:18-alpine AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy only the my-app directory into the container
COPY my-app/package*.json ./my-app/

# Navigate to the my-app directory and install dependencies
WORKDIR /app/my-app
RUN npm install

# Copy the rest of the application code
COPY my-app/ .

# Build the application for production
RUN npm run build

# Use a lightweight web server for serving the production build
FROM nginx:alpine AS production

# Copy the built files from the builder stage
COPY --from=builder /app/my-app/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]