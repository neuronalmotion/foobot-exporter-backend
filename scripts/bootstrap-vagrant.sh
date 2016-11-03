#!/usr/bin/env bash

BASE_DIR=/vagrant
VENV_DIR=$BASE_DIR/venv

export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
export LC_CTYPE="en_US.UTF-8"
locale-gen en_US.UTF-8
dpkg-reconfigure locales

printstage(){
    echo "--------------------------------------------------------------"
    echo $1
    echo "--------------------------------------------------------------"
}

printstage "Installing packages"

apt-get update
apt-get install -y \
    	gcc \
    	gettext \
        blender \
        cmake \
        debconf-utils \
        libgeos-dev \
        libspatialindex-dev \
        openscad \
        python3-dev \
        python3-pip


pip3 install --upgrade pip
pip3 install virtualenv

printstage "Initializing virtualenv"

cd $BASE_DIR

virtualenv $VENV_DIR
. $VENV_DIR/bin/activate

cp foobot_exporter/local_settings.py.template foobot_exporter/local_settings.py
pip install -r requirements.txt

python manage.py migrate

echo ". $VENV_DIR/bin/activate ; cd $BASE_DIR" >> /home/vagrant/.bashrc

