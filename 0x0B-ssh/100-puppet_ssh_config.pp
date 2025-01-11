file_line { 'Turn off passwd auth':
    path => '/home/your_user/.ssh/config',
    line => 'PasswordAuthentication no',
    require => Package['openssh-client'],
}

file_line { 'Declare identity file':
    path => '/home/your_user/.ssh/config',
    line => 'IdentityFile ~/.ssh/school',
    require => Package['openssh-client'],
}
