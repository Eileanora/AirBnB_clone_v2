#!/usr/bin/env bash
# bash script that sets up your web servers for the deployment.

# install nginx if not already installed
sudo apt-get -y update
sudo apt-get -y install nginx

# create folders if not already created
sudo mkdir -p /data/web_static/releases/test/

# create fake html file
sudo echo "my test file" | sudo tee /data/web_static/releases/test/index.html

# create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# give ownership of /data/ folder to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i "/server_name _;/a \
\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

# restart nginx
sudo service nginx restart
