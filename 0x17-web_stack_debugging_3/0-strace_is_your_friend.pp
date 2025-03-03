# Fixes Apache 500 error by correcting PHP file extension in WordPress settings
exec { 'fix-wordpress':
  command => 'sed -i s/class-wp-locale.phpp/class-wp-locale.php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
