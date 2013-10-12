# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # Start from closest model to Travis CI
  # http://about.travis-ci.org/docs/user/ci-environment/#CI-environment-OS
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  # Set up variables
  $install_env_vars = <<SCRIPT
    # Set the term to be xterm for SSH sessions
    if ! grep TERM /etc/environment ; then
      echo 'TERM=xterm' >> /etc/environment
    fi

    # If SUBLIME_TEXT_VERSION hasn't been set, set and persist it
    export SUBLIME_TEXT_VERSION=3.0
    if ! grep SUBLIME_TEXT_VERSION /etc/environment; then
      echo 'SUBLIME_TEXT_VERSION=$SUBLIME_TEXT_VERSION' >> /etc/environment
    fi
SCRIPT
  config.vm.provision "shell", inline: $install_env_vars

  $install_sublime = <<SCRIPT
    # If Sublime Text isn't installed, install it
    if test -z "$(which sublime_text)"; then
      # Preparation for install script
      sudo apt-get update
      sudo apt-get install python-software-properties -y
      sudo mkdir -p /usr/share/icons/hicolor/16x16/apps/
      sudo mkdir -p /usr/share/icons/hicolor/32x32/apps/
      sudo mkdir -p /usr/share/icons/hicolor/48x48/apps/
      sudo mkdir -p /usr/share/icons/hicolor/128x128/apps/
      sudo mkdir -p /usr/share/icons/hicolor/256x256/apps/

      # Install Sublime Text
      cd /vagrant
      ./test/install.sh

      # Output the version
      sublime_text --version
    fi
SCRIPT
  config.vm.provision "shell", inline: $install_sublime

  $install_xvfb = <<SCRIPT
    # If xvfb isn't installed, install it
    if ! test -f /usr/bin/Xvfb; then
      sudo apt-get install xvfb libgtk2.0-0 -y
    fi
SCRIPT
  config.vm.provision "shell", inline: $install_xvfb

  $install_package = <<SCRIPT
    cd /vagrant
    sudo apt-get install python-pip -y
    python setup.py develop
SCRIPT
  config.vm.provision "shell", inline: $install_package

  $launch_xvfb = <<SCRIPT
    # Set and persist DISPLAY to :99.0
    export DISPLAY=:99.0
    if ! grep DISPLAY /etc/environment ; then
      echo 'DISPLAY=$DISPLAY' >> /etc/environment
    fi

    # Set up Xvfb
    /usr/bin/Xvfb $DISPLAY -screen 0 1024x768x24 &
SCRIPT
  config.vm.provision "shell", inline: $launch_xvfb

  # When done, vagrant ssh
  # cd /vagrant
  # SUBLIME_TESTS_AUTO_KILL=TRUE ./test.sh
end
