class { 'nginx': }

file { '/var/www/html/index.html':
    ensure => file,
    content => 'Hello World!',
}

file { '/var/www/html/404.html':
    ensure => file,
    content => "Ceci n'est pas une page",
}

nginx::resource::vhost { 'localhost':
    listen_port => 80,
    server_name => 'localhost',
    root => "/var/www/html",
    index_file => 'index.html',
    error_page => {
        '404' => '/404.html',
    },
}

nginx::resource::proxy { 'redirect_me':
    ensure => present,
    vhost => 'localhost',
    proxy_pass => 'https://www.youtube.com/watch?v=QH2-TGUlwu4',
    redirect => 'permanent',
}
