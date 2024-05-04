#!/usr/bin/env bash

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get install -y nginx

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i '/server_name _;/a location /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
