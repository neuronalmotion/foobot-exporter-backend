from fabric.api import *

def prepare_dev_environment():
    local('sudo ansible-galaxy install -r ansible/requirements.yml')

def install():
    local('ansible-playbook --tags install ansible/site.yml')

def deploy():
    local('ansible-playbook --tags deploy ansible/site.yml')

