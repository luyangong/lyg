# 更新github ssh key


## 1. 生成pub key
```bash
ssh-keygen -t rsa -b 4096 -C "your email address"
```
# 2.复制到github

复制 ~/.ssh/id_rsa.pub的内容到github

## 3.设置remote-url
```bash
git remote set-url origin git@github.com:luyangong/lyg.git
```
done!

