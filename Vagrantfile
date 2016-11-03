# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  # due to a bug in the latest ubuntu/xenial64
  # https://bugs.launchpad.net/cloud-images/+bug/1565985
  # we cannot use this vagrant image yet
  config.vm.box = "ubuntu/trusty64"
 
  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
    v.cpus = 2
  end

  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 8000, host: 8001

  config.vm.provision :shell, path: "scripts/bootstrap-vagrant.sh"

end
