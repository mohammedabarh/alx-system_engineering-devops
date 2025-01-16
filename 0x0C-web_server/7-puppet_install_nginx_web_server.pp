# This Puppet script installs and configures Nginx to serve a "Hello World!" page
# and sets up a redirect for /redirect_me to a specified URL.

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Create the index.html file with "Hello World!" content
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

# Configure Nginx to redirect /redirect_me to a specified URL
file_line { 'redirect_me':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/@cryptoappcodergroup permanent;',
  notify => Service['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
