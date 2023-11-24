# Configuration to install python flask

# make sure pip is installed
package { 'python3-pip':
  ensure => installed,
}

# install flask here
exec { 'install-flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => '/usr/local/bin:/usr/bin',
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
  require => Package['python3-pip'],
}
