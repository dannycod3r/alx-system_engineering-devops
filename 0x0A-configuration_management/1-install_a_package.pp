# Configuration to install python flask

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
