# 0-strace_is_your_friend.pp
# This Puppet manifest fixes an Apache 500 error in a WordPress installation
# by correcting a typo in the wp-settings.php file where "php" was misspelled as "phpp"

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin:/usr/bin:/bin',
  onlyif  => 'test -f /var/www/html/wp-settings.php',
}
