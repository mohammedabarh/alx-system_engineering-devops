# 0-strace_is_your_friend.pp
# Fixes a WordPress file that causes Apache to return 500 error

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/bin/:/bin/'
}
