# Kill process named killmenow

exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin:/bin',
  onlyif  => 'pgrep killmenow',
}
