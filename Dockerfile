FROM nginx:alpine

# Copy hardened nginx configuration with security headers
COPY nginx-hardened.conf /etc/nginx/conf.d/default.conf

# Copy application static files
COPY . /usr/share/nginx/html/

# Clean non-web files from webroot
RUN rm -f /usr/share/nginx/html/nginx-hardened.conf \
          /usr/share/nginx/html/test_jarvis.py \
          /usr/share/nginx/html/Dockerfile \
          /usr/share/nginx/html/docker-compose.yml

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
