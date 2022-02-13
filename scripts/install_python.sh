#!/bin/bash

read -p "Input the python version, default:3.8.10? " v
if [ ! $v ]; then 
    v="3.8.10"
fi
wget https://cdn.npm.taobao.org/dist/python/$v/Python-${v}.tar.xz -P ~/.pyenv/cache
pyenv install $v
# pyenv local $v

