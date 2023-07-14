# the first stage of the build will use a Node alpine 3.11 image
FROM node:alpine as builder

# set the working directory in the container
WORKDIR /app

# copies package.json and package-lock.json to Docker environment
COPY package*.json ./

# Install all node packages
RUN npm ci 

# Copy all files from current directory to docker
COPY . .

# Build application
RUN npm run build

# the second stage of the build will use a nginx alpine image
FROM nginx:alpine

# Copy the build output from the previous stage
COPY --from=builder /app/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
