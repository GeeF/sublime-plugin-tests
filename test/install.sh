#!/bin/sh

# TODO: See if we can get a plugin to output a simple file
# TODO: See if it will run in a VM
# TODO: What happens if we connect an x11-forwarding?

# If we are to install Sublime Text 2
if test $SUBLIME_TEXT_VERSION = "2.0"; then
  # http://askubuntu.com/questions/172698/how-do-i-install-sublime-text-2
  sudo add-apt-repository ppa:webupd8team/sublime-text-2 -y
  sudo apt-get update
  sudo apt-get install sublime-text -y
  sudo ln -s /usr/bin/subl /usr/bin/sublime_text
elif test $SUBLIME_TEXT_VERSION = "3.0"; then
  sudo add-apt-repository ppa:webupd8team/sublime-text-3 -y
  sudo apt-get update
  sudo apt-get install sublime-text-installer -y
  sudo ln -s /usr/bin/subl /usr/bin/sublime_text
fi