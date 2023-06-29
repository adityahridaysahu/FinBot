# Specify the base image
FROM node:14-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock) to the container
COPY package*.json ./

RUN npm cache clean --force
RUN npm install -g npm@latest


# Install dependencies
RUN npm install

# Copy the application code to the container
COPY . .

# Build the production-ready code
RUN npm run build

EXPOSE 3000

# Set the command to start the application
CMD ["npm", "start"]
