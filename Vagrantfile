# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "forwarded_port", guest: 8025, host: 8025
  config.vm.provision "shell", inline: $shell
  config.vm.provision "shell", path: "get-mailhog.bash"
end

$shell = <<-'CONTENTS'
  apt-get update
  apt-get install -y python3-pip
  pip3 install virtualenv
CONTENTS

# 2018.10.24-DEA
