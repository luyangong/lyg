#!/bin/bash
set -e

# 下载pyenv
git clone https://gitee.com/mirrors/pyenv.git ~/.pyenv

# 修改环境变量, 如果用的是bash, 就是~/.bashrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

# 重启shell
exec "$SHELL"
