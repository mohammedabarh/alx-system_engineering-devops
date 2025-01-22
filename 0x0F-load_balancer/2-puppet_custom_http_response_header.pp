# Puppet manifest to configure Nginx with a custom HTTP response header

class { 'nginx':
  package_ensure => 'installed',
}

file { '/etc/nginx/conf.d/custom_header.conf':
  ensure  => 'file',
  content => "server {
    listen 80;
    server_name _;

    add_header X-Served-By \$HOSTNAME;

    location / {
        root /var/www/html;
        index index.html;
    }
}\n",
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => 'running',
  enable => true,
}
