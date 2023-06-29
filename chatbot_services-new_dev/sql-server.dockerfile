FROM mysql:latest

# Set the root password for MySQL
ENV MYSQL_ROOT_PASSWORD=bestchatbot

# Create the database and tables
COPY tables.sql /docker-entrypoint-initdb.d/

# Expose the default MySQL port
EXPOSE 3306
