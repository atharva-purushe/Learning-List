# HTTPS Implementation

## Objective
Upgrade a web server to serve content over HTTPS using Docker.

## Tasks Completed
1. Generated Self-Signed SSL Certificate:
   - Used OpenSSL to create `certificate file.crt` and `Private key.key`.
   - Command: `openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout Private key.key -out certificate file.crt`.
   - Ran this in `C:\Users\Atharva Purushe\Internet-Networking\HTTP-HTTPS\` and provided `localhost` as the common name.
2. Created Configuration Files:
   - Created `ssl.conf` to configure Apache for HTTPS.
   - Created `httpd.conf` to include `ssl.conf` with: `Include conf/ssl.conf`.
3. Built and Ran a Docker Container:
   - Without ngrok and created a `Dockerfile` to set up the Apache server:
   - Built the image: `docker build -t my-apache-https .`.
   - Ran the container: `docker run -d -p 443:443 --name my-apache-https-container my-apache-https`.
   - Accessed it directly at `https://localhost` and confirmed a secure connection.
4. With ngrok 
   - Installed ngrok and ran it to expose the local server: `ngrok http 443`.
   - Obtained a public URL


## Deliverables 
1. HTTP and HTTPS transactions : I explore how HTTP & HTTPS protocols operate by interacting with a public API using GET and POST requests and then analysed the response structure, headers and status codes. Using docker I ran a Apache server to serve a custom html file Index.html over HTTP making it accessible via local host. This allowed me to understand how unencrypted HTTP transmits data between a client and server.
2. I have then upgraded the setup to https by generating a self-signed SSL certificate using OpenSSL and modifying Apache's configuration (httpd.conf and ssl.conf) to enable SSL on port 443. A new container was build to serve the same content over https://localhost, ensuring encryption. Instead of copying files into a running container, I directly customized the image local by modifying its configuration files and adding my index.html file.
3. Finally, I used ngrok to expose the local server to the internet via a publicly accessible HTTPS url. Ngrok creates a public HTTPS endpoint and provides a valid SSL certificate. It creates a secure tunnel using its own SSL certificate and acts as a middleman to handle the encryption and public access.