# Puppet manifest to install nginx
package { 'nginx':
  ensure => installed,
}

# Nginx config
file_line { 'redirect_me':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

# Nginx config
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Restart nginx
exec { 'restart service':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}
