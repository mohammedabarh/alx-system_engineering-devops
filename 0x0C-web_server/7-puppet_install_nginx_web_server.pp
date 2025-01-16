# Install Nginx server, setup and configuration

package { 'nginx':
  ensure => 'installed',
}

# Create the index.html file with "Hello World"
file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World',
}

# Configure Nginx to redirect /redirect_me
file_line { 'redirect_me':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  line   => 'rewrite ^/redirect_me https://www.youtube.com permanent;',
  require => Package['nginx'],
}

# Ensure the Nginx service is running
service { 'nginx':
  ensure => running,
  enable => true,  # Ensure Nginx starts on boot
  subscribe => File['/etc/nginx/sites-available/default'],  # Restart if the config file changes
}
