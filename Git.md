# 工作中的Git

## 问题

### 仓库里记录了敏感资料怎么处理？

1. 删除仓库里所有的记录。

`git filter-branch -f --tree-filter 'rm -rf models.pyc' HEAD`

2. 推送到远程仓库

`git push  --force --all`

