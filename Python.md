# Python 的学习笔记和工作总结

## 问题

1. [ ] 语句和表达式的区别？为什么有这两个概念？他们分别是什么意思？


## 文档

### 问题

1. [ ] 编写文档可以用什么语言？
1. [ ] 参数的文档怎么写？
1. [ ] 返回值呢？



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
