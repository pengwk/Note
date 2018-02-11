# 工作中的Git

## 问题

### 仓库里记录了敏感资料怎么处理？

需要删除仓库里所有的记录。

`git filter-branch -f --tree-filter 'rm -rf models.pyc' HEAD`

