# Fixes Apache 500 error by correcting PHP file extension in WordPress settings
exec { 'fix-wordpress':
  command => 'sed -i "s/\.phpp/.php/" /var/www/html/wp-settings.php',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
