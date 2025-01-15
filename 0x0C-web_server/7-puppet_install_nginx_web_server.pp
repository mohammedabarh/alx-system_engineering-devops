# Install NginX
package { 'nginx':
  ensure => 'installed'
}

file { '/var/www/html/index.html':
  content => 'Hello World',
}

file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com@cryptoappcodergroup permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
