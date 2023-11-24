# Manifest file to kill a process

exec { 'pkill killmenow':
  path    => ['/usr/bin', '/usr/sbin',]
}