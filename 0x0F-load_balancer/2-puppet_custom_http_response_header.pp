#!/usr/bin/env bash
# Puppet manifest to configure Nginx with a custom HTTP response header

exec { 'http header':
        command => 'sudo apt-get update -y;
        sudo apt-get install nginx -y;
        sudo se -i "/server_name_/a add_header X-Served-By HOSTNAME;" /etc/nginx/sites-available/default
        sudo service nginx restart',
        provider => shell,

}
