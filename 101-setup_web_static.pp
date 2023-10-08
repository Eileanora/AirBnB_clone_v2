# puppet script to do the same thing as the task 0-setup_web_static.sh

package { 'nginx':
  ensure => present,
}

file { '/data':
  ensure => directory,
}

file { '/data/web_static':
  ensure  => directory,
  require => File['/data'],
}

file { '/data/web_static/releases':
  ensure  => directory,
  require => File['/data/web_static'],
}

file { '/data/web_static/shared':
  ensure  => directory,
  require => File['/data/web_static'],
}

file { '/data/web_static/releases/test':
  ensure  => directory,
  require => File['/data/web_static/releases'],
}

file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => "
    <html>
      <head>
      </head>
      <body>
        Holberton School
      </body>
    </html>",
  require => File['/data/web_static/releases/test'],
}

file { '/data/web_static/current':
  ensure  => link,
  target  => '/data/web_static/releases/test',
  require => File['/data/web_static/releases/test'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {
                try_files \$uri \$uri/ =404;
        }

        location /hbnb_static {
                alias /data/web_static/current;
        }
    }",
}

service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/sites-available/default'],
}
