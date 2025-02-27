# 0-strace_is_your_friend.pp
# Fixes a WordPress file that causes Apache to return 500 error

# Ensure the required PHP module is installed
package { 'php5-mysql':
  ensure => installed,
}

# Ensure the Apache service is running
service { 'apache2':
  ensure => running,
  enable => true,
}

# Set the correct permissions for the WordPress directory
file { '/var/www/html':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  recurse => true,
}

# Fix the WordPress configuration file
exec { 'fix-wordpress':
  command     => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path        => ['/usr/local/bin/', '/bin/'],
  refreshonly => true,
  subscribe   => File['/var/www/html'],
}

# Restart Apache to apply changes
exec { 'restart-apache':
  command     => '/usr/sbin/service apache2 restart',
  refreshonly => true,
  subscribe   => [File['/var/www/html'], Exec['fix-wordpress']],
}
