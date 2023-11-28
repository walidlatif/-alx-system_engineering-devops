# install Flask v2.1.0
package { 'python3':
  ensure => installed,
}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
