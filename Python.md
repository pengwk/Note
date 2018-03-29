# Python 的学习笔记和工作总结

## 常用数据结构的Python实现

- int 内存池 预先分配，申请使用

[深入 Python 整数对象的实现](http://python.jobbole.com/82632/)

- str

#### list

> 在Python的官方实现中，list就是一种采用**分离式**技术实现的动态顺序表，其性质都源于这种实现方式。Python的list采用了前面介绍的元素储存区调整策略，如果需要反复加入元素，用`lst.insert(len(lst), x)`比在一般位置插入元素的效率高。Python提供了另一等价写法`lst.append(x)`，如果合适就应优先选用。
在Python系统中，list实现采用了如下实际策略：在建立空表（或者很小的表）时，系统分配一块能容纳8个元素的储存区；在执行插入操作（insert或append等）时，如果元素区满就换一块4倍大的储存区。但如果当时的表已经很大，系统将改变策略，换储存区时容量加倍。这里的“很大”是一个实现确定的参数，目前的值是50000.引入后一个策略是为了避免出现过多空闲的储存位置。如前所述，通过这套技术实现的list，尾端加入元素操作的平均时间复杂度是O(1)。《数据结构与算法 Python语言描述》


- tuple [tʌpl] 和list大致相同，不过没有修改的功能。

#### dict set

字典和集合类型都是基于散列表技术实现的数据结构，采用内消解的技术解决冲突。下面介绍一些细节，以dict为例。

- dict类型的对象采用散列表技术实现，其元素是key-value（关键码-值）对，关键码可以使任何不变对象，值可以是任何对象。
- 在创建空字典或者很小的字典时，初始分配的储存区可容纳8个元素。
- dict对象在负载因子超过2/3时自动更换更大的储存区，并把已经保存的内容重新散列到新的储存区。如果当前字典对象不太大，就按当时字典中的实际元素的4倍分配新储存区。当字典的元素超过50000（5万）时，改为按实际个数的2倍分配新储存区。

## 垃圾回收

三种方式的优缺点，相关API，可能会遇到的问题。

容器对象：list,dict,tuple,instance

### 三种方式

1. 引用计数 Reference Counting，无法处理循环引用
2. 标记清除 Mark Sweep，基于追踪回收(tracing GC)的技术实现的垃圾回收算法.作用对象：**容器对象**
3. 分代回收 Generational Garbage Collection，分代回收建立在**标记清除**基础上。 作用对象：**容器对象**。

### 内存泄漏

例子，调试，处理

### 相关API

`gc`模块,常用操作

#### 参考

- [伯乐在线：Python 中的垃圾回收机制](http://python.jobbole.com/87843/?utm_source=blog.jobbole.com&utm_medium=relatedPosts)
- [gc — Garbage Collector interface](https://docs.python.org/2/library/gc.html)
- [Ruby 画说 Ruby 与 Python 垃圾回收](https://ruby-china.org/topics/28127)
- [[转载]Python垃圾回收机制--完美讲解!](https://www.jianshu.com/p/1e375fb40506)
- [gc – Garbage Collector](https://pymotw.com/2/gc/)
- [term-generational-garbage-collection](http://www.memorymanagement.org/glossary/g.html#term-generational-garbage-collection)

## 各种数据类型

基本、高阶 原理，实现

## 代码规范

pep8、自动检查工具、实现原理

## 装饰器

## 运算符


## 生成器

原理、实现



## 协程 

原理，事件循环event loop，python2.x, python3.x的的区别，新的语法，自己实现，

#### 参考

- [深入理解Python中协程的应用机制： 使用纯Python来实现一个操作系统吧！](http://blog.csdn.net/worisaa/article/details/63683102)
- [A Curious Course on Coroutines and Concurrency](http://www.dabeaz.com/coroutines/)

## 线程

线程、进程的区别与联系，相关API，如何转换，并发，thread_local, 线程安全，锁，线程间通信，

## 进程

## 

## 问题

1. [ ] 语句和表达式的区别？为什么有这两个概念？他们分别是什么意思？


## 文档

### 问题

1. [ ] 编写文档可以用什么语言？
1. [ ] 参数的文档怎么写？
1. [ ] 返回值呢？

## 调试

## 

python -m pdb server.py 


### gbd

1. 安装GDB

```bash
sudo apt-get install gdb
```

2. 导入Python

```
file python
```

3. 运行脚本

```
run server.py
```

4. 退出

```
Quit
```

#### 分析coredump

```
gdb --core=core.12
```

#### 例子

(gdb) file python
Reading symbols from python...(no debugging symbols found)...done.
(gdb) run server.py -p 7801
Starting program: /usr/bin/python server.py -p 7801
warning: Error disabling address space randomization: Operation not permitted
During startup program terminated with signal SIGSEGV, Segmentation fault.


## 工作感悟

第一份工作，在一家小公司实习，维护原有代码，修复BUG，配合同事调试，开发新功能（前端Vue），

使用Python Tornado做TCP服务器，Redis做消息队列，Nginx做Web Server，Supervisor运行整套服务，使用Vue构建SPA应用，PHP Lavarel做网站后端，使用MySQL做数据库。

### 类型与数据结构

这两个真的非常重要，Python是强类型、动态语言（strongly,dynamically typed language）,

- 动态，运行时可以转换类型。
- 强类型，变量本身有类型的区别。

把返回的数据类型和数据的结构写的清楚明了真的很重要，修复bug的时候，问题就出现，很多时候不知道那里面有什么。变过来变过去就蒙了。

> 动态类型一时爽，代码重构火葬场。不是没有道理（捂脸）。

#### type 与 isinstance

`type`与`isinstance`都能判别一个对象的类型，他们对子类的处理是不同的。

- `type(object)` 返回继承链上最新的类型。
- `isinstance(object, type_name)`继承链上任意一个类型都会返回`True`。

#### Python代码

**问题**
______

1. [ ] 代码中有`sys.path.append('../')`是干嘛的？
2. [ ] TCP传输中数据包没有接收完整，为什么？


**回答**
_____

1.

为了能导入父级模块。

#### 2

TCP里传输的是JSON字符串，Tornado接收到后解析出错，日志显示数据没有完整接收（收到1439字节，发送了2414字节）

发送时间间隔很快时（1,2秒）出现，将时间调至5秒时，就没有问题了。

**初步判断**

网络质量差，传输数据过大，TCP分包传送，当一部分数据包抵达后就返回了。Tornado代码如下：

```python
        self.stream.read_bytes(num_bytes=TornadoTCPConnection.MAX_SIZE,
                               callback=stack_context.wrap(self.on_message_receive), partial=True)
```

猜测与`partial`有关，这个参数设置为真会导致缓冲区有可用数据就会调用回调函数，导致数据没有接收完整。TCP是流，没有消息边界，后面传输的数据包就没有处理。
