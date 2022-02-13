#!/bin/bash

if [ ! -d ~/.virtualenvs ]; then
    echo "Create dir: ~/.virtualenv"
    mkdir ~/.virtualenvs
fi

read -p "Input the venv name, default:venv?" venv
if [ ! $venv ]; then 
    venv="venv"
fi
python -m venv ~/.virtualenvs/$venv
source ~/.virtualenvs/$venv/bin/activate

