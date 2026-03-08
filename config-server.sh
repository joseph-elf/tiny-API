#!/usr/bin/env bash


# USERNAME on the server
USERNAME=ubuntu

# IP of the server
IP=$(curl -s https://api.ipify.org)

# SSH key file
SSH_KEY=~/.ssh/api-rene.pem

#Git-Hub repository of this project
GIT_HUB_servertoolbox=https://github.com/joseph-elf/server-toolbox.git

#Git-Hub repositories to load (as an array or not)
GIT_HUB_repos=(
https://github.com/joseph-elf/tiny-API.git
)


# Version of Python
PYTHON_VERSION=3.12
VENV_NAME=venv
