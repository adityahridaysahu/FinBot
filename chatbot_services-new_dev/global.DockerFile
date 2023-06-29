# Use the official Python base image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Install build tools
RUN apk update && \
    apk add --no-cache build-base
    

# Install MySQL or MariaDB development libraries
RUN apk update && \
    apk add --no-cache mariadb-connector-c-dev

# Copy the requirements file and install dependencies
COPY . /app
RUN pip install -r requirements.txt

# Configure MySQL
ENV MYSQL_DATABASE=globalDB
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=bestchatbot
ENV MYSQL_HOST=172.20.139.14


# Copy the app code to the container

# Expose the desired port (e.g., 5000)
EXPOSE 7000

# Set the command to run the Flask app
CMD ["python", "global_routes.py"]
