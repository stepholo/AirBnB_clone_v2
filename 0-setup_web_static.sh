#!/usr/bin/env bash
# Sets up the web servers for the deployment of web-static

# Check if nginx is not installed and install
if ! command -v nginx &> /dev/null; then
	sudo apt update
	sudo apt install -y nginx
fi

# Set the upropriate firewall
sudo ufw allow 'Nginx HTTP'

# Create the required folder if it doesn't exits
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file with simple content to test nginx configuration
echo "Web-static Deployment!" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link. If the symbolic link already exists. It should be deleted and
# and recreated every time the script is ran.
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
# This should be recursive; everything inside should be created/owned by this user/group.
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
# Use alias inside your Nginx configuration
web_static_path="/data/web_static/current"
alias_name="hbnb_static"
nginx_config="/etc/nginx/sites-available/default"

sudo sh -c "echo 'server {
	listen 80 default_server;
	listen [::]:80 default_server;
	add_header X-Served-By $HOSTNAME;
	root /var/www/html;
	index index.html index.htm;

	location /$alias_name {
		alias $web_static_path/;
		index index.html index.htm;
	}
	
	location /redirect_me {
		return 301 http://cuberule.com/;
	}

	error_page 404 /404.html;
	location /404 {
		root /var/www/html;
		internal;
	}
}' > $nginx_config"


# Restart nginx to apply changes
sudo service nginx restart
