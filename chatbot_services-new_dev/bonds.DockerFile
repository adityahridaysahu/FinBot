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
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Copy the app code to the container
COPY . /app


# Configure MySQL
ENV MYSQL_DATABASE=bondsDB
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=bestchatbot
ENV MYSQL_HOST=172.20.139.14

# Expose the desired port (e.g., 5000)
EXPOSE 9000

# Set the command to run the SQL script and Flask app
CMD ["python", "bond_routes.py"]

