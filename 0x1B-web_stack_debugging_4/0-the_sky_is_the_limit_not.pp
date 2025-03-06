# 0-the_sky_is_the_limit_not.pp
# Fixes Nginx to handle high amounts of requests

exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx && service nginx restart',
  path    => '/usr/local/bin/:/bin/:/usr/bin/:/usr/sbin/',
}
