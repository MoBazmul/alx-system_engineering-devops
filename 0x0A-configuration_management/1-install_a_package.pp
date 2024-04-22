#!/usr/bin/pup
# Using Puppet to install flask from pip3

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => ['/usr/bin'],
  unless  => '/usr/bin/flask --version | grep "2.1.0"',
}
