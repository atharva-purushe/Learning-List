FROM httpd:latest

# Copy configs
COPY httpd.conf /usr/local/apache2/conf/httpd.conf
COPY ssl.conf /usr/local/apache2/conf/ssl.conf

# Copy certificate and key
COPY apache-selfsigned.crt /usr/local/apache2/conf/
COPY apache-selfsigned.key /usr/local/apache2/conf/

# Copy HTML
COPY index.html /usr/local/apache2/htdocs/index.html

# Expose HTTPS port
EXPOSE 443
