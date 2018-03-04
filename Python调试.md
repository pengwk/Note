# 调试

分析coredump文件

## Linux动态链接库 调试

LD_DEBUG = [help, all]

http://www.bnikolic.co.uk/blog/linux-ld-debug.html

man dlopen

lsof

ldd

### 查看需要加载的动态链接库

```
ldd `which python`
```

```
root@localhost:~# ldd `which python`
	linux-vdso.so.1 =>  (0x00007ffe08bb3000)
	libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007fe8f1f0d000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fe8f1b43000)
	libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007fe8f193f000)
	libutil.so.1 => /lib/x86_64-linux-gnu/libutil.so.1 (0x00007fe8f173c000)
	libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007fe8f1522000)
	libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fe8f1219000)
	/lib64/ld-linux-x86-64.so.2 (0x00007fe8f212a000)

```

### 系统信息

#### 文件查找

locate

find

#### 操作系统信息

uname -a

cat /proc/version

root@localhost:~# lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 16.04.2 LTS
Release:	16.04
Codename:	xenial

#### 操作系统日志

dmesg

dmesg | less 

ls -alh /var/log/

## 开启

ulimit -c 

ulimit -c unlimited

## 工具

https://wiki.python.org/moin/DebuggingWithGdb

### gdb

#### 寄存器

```
(gdb) info registers 
rax            0x9343c0	9651136
rbx            0x7fda35f41be8	140575184788456
rcx            0x0	0
rdx            0x1a35f10	27483920
rsi            0x7fda388d7b28	140575228394280
rdi            0xffffffff	4294967295
rbp            0x7fda35f3e910	0x7fda35f3e910
rsp            0x7ffe5a8c1fb8	0x7ffe5a8c1fb8
r8             0x19eb950	27179344
r9             0x7100	28928
r10            0x5	5
r11            0x4	4
r12            0x1a47330	27554608
r13            0x0	0
r14            0x1a4a760	27567968
r15            0x0	0
rip            0x1956e	0x1956e
eflags         0x10206	[ PF IF RF ]
cs             0x33	51
ss             0x2b	43
ds             0x0	0
es             0x0	0
fs             0x0	0
gs             0x0	0

```

$rip 指令寄存器，指向当前执行的代码位置
$rsp 栈指针寄存器，指向当前栈顶
$rax，$rbx，$rcx，$rdx，$rsi，$rdi，$rbp，$r8，$r9，$r10，$r11，$r12，$r13，$r14，$r15 通用寄存器

#### 常用命令

info register
info frame
info args
info locals

watch

set


where bt file run step b r  print c display help

gdb -c core

gdb -p 1000 (pid number)

py-bt

quit q

py-list


```
backtrace -- Print backtrace of all stack frames
bt -- Print backtrace of all stack frames
down -- Select and print stack frame called by this one
frame -- Select and print a stack frame
py-bt -- Display the current python frame and all the frames within its call stack (if any)
py-bt-full -- Display the current python frame and all the frames within its call stack (if any)
py-down -- Select and print the python stack frame called by this one (if any)
py-up -- Select and print the python stack frame that called this one (if any)
return -- Make selected stack frame return to its caller
select-frame -- Select a stack frame without printing anything
up -- Select and print stack frame that called this one
```

## 重新编译Python

clone官方库


## 教程

[gdb调试秘籍（寄存器、栈）](http://blog.csdn.net/linux_vae/article/details/79241278)

[GDB调试汇编堆栈过程分析](https://www.cnblogs.com/lxm20145215----/p/5982554.html)

[gdb 调试入门，大牛写的高质量指南](http://blog.jobbole.com/107759/)

[gdb Debugging Full Example (Tutorial): ncurses](https://zhuanlan.zhihu.com/p/28769268)

[gdb-example-ncurses](http://www.brendangregg.com/blog/2016-08-09/gdb-example-ncurses.html)

[segmentation-fault-core-dump-in-python-c-extension](https://stackoverflow.com/questions/29396600/segmentation-fault-core-dump-in-python-c-extension)

## 共享库

root@localhost:~# nm -D /usr/lib/python2.7/lib-dynload/_ssl.x86_64-linux-gnu.so


### 例子

```gdb
root@localhost:~# gdb
GNU gdb (Ubuntu 7.11.1-0ubuntu1~16.5) 7.11.1
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word".
(gdb) file python
Reading symbols from python...(no debugging symbols found)...done.
(gdb) run test.py
Starting program: /usr/bin/python test.py
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
warning: Corrupted shared library list: 0xa369d0 != 0xa50dd0

Program received signal SIGSEGV, Segmentation fault.
0x000000000001956e in ?? ()
(gdb) where
#0  0x000000000001956e in ?? ()
#1  0x00007ffff59f7d69 in SSL_load_error_strings () from /usr/local/lib/python2.7/dist-packages/mysql-vendor/libssl.so.1.0.0
#2  0x00007ffff4fc8c1d in init_ssl () from /usr/lib/python2.7/lib-dynload/_ssl.x86_64-linux-gnu.so
#3  0x000000000051a911 in _PyImport_LoadDynamicModule ()
#4  0x00000000004a4ae1 in ?? ()
#5  0x00000000004a42c9 in PyImport_ImportModuleLevel ()
#6  0x00000000004a59e4 in ?? ()
#7  0x00000000004a577e in PyObject_Call ()
#8  0x00000000004c5e10 in PyEval_CallObjectWithKeywords ()
#9  0x00000000004be6d7 in PyEval_EvalFrameEx ()
#10 0x00000000004b9ab6 in PyEval_EvalCodeEx ()
#11 0x00000000004b97a6 in PyEval_EvalCode ()
#12 0x00000000004b96df in PyImport_ExecCodeModuleEx ()
#13 0x00000000004b2b06 in ?? ()
#14 0x00000000004a4ae1 in ?? ()
#15 0x00000000004a45dd in PyImport_ImportModuleLevel ()
#16 0x00000000004a59e4 in ?? ()
#17 0x00000000004a577e in PyObject_Call ()
#18 0x00000000004c5e10 in PyEval_CallObjectWithKeywords ()
#19 0x00000000004be6d7 in PyEval_EvalFrameEx ()
#20 0x00000000004b9ab6 in PyEval_EvalCodeEx ()
#21 0x00000000004b97a6 in PyEval_EvalCode ()
#22 0x00000000004b96df in PyImport_ExecCodeModuleEx ()
#23 0x00000000004b2b06 in ?? ()
#24 0x00000000004a4ae1 in ?? ()
#25 0x00000000004a42c9 in PyImport_ImportModuleLevel ()
#26 0x00000000004a59e4 in ?? ()
#27 0x00000000004a577e in PyObject_Call ()
#28 0x00000000004c5e10 in PyEval_CallObjectWithKeywords ()
#29 0x00000000004be6d7 in PyEval_EvalFrameEx ()
#30 0x00000000004b9ab6 in PyEval_EvalCodeEx ()
#31 0x00000000004b97a6 in PyEval_EvalCode ()
#32 0x00000000004b96df in PyImport_ExecCodeModuleEx ()
#33 0x00000000004b2b06 in ?? ()
#34 0x00000000004a4ae1 in ?? ()
#35 0x00000000004a42c9 in PyImport_ImportModuleLevel ()
#36 0x00000000004a59e4 in ?? ()
#37 0x00000000004a577e in PyObject_Call ()
#38 0x00000000004c5e10 in PyEval_CallObjectWithKeywords ()
---Type <return> to continue, or q <return> to quit---
#39 0x00000000004be6d7 in PyEval_EvalFrameEx ()
#40 0x00000000004b9ab6 in PyEval_EvalCodeEx ()
#41 0x00000000004b97a6 in PyEval_EvalCode ()
#42 0x00000000004b96df in PyImport_ExecCodeModuleEx ()
#43 0x00000000004b2b06 in ?? ()
#44 0x00000000004b402c in ?? ()
#45 0x00000000004a4ae1 in ?? ()
#46 0x00000000004a4513 in PyImport_ImportModuleLevel ()
#47 0x00000000004a59e4 in ?? ()
#48 0x00000000004a577e in PyObject_Call ()
#49 0x00000000004c5e10 in PyEval_CallObjectWithKeywords ()
#50 0x00000000004be6d7 in PyEval_EvalFrameEx ()
#51 0x00000000004b9ab6 in PyEval_EvalCodeEx ()
#52 0x00000000004eb30f in ?? ()
#53 0x00000000004e5422 in PyRun_FileExFlags ()
#54 0x00000000004e3cd6 in PyRun_SimpleFileExFlags ()
#55 0x0000000000493ae2 in Py_Main ()
#56 0x00007ffff7810830 in __libc_start_main (main=0x4934c0 <main>, argc=2, argv=0x7fffffffe648, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, 
    stack_end=0x7fffffffe638) at ../csu/libc-start.c:291
#57 0x00000000004933e9 in _start ()
(gdb) bt
#0  0x000000000001956e in ?? ()
#1  0x00007ffff59f7d69 in SSL_load_error_strings () from /usr/local/lib/python2.7/dist-packages/mysql-vendor/libssl.so.1.0.0
#2  0x00007ffff4fc8c1d in init_ssl () from /usr/lib/python2.7/lib-dynload/_ssl.x86_64-linux-gnu.so
#3  0x000000000051a911 in _PyImport_LoadDynamicModule ()
#4  0x00000000004a4ae1 in ?? ()
#5  0x00000000004a42c9 in PyImport_ImportModuleLevel ()
#6  0x00000000004a59e4 in ?? ()
#7  0x00000000004a577e in PyObject_Call ()
#8  0x00000000004c5e10 in PyEval_CallObjectWithKeywords ()
#9  0x00000000004be6d7 in PyEval_EvalFrameEx ()
#10 0x00000000004b9ab6 in PyEval_EvalCodeEx ()
#11 0x00000000004b97a6 in PyEval_EvalCode ()
#12 0x00000000004b96df in PyImport_ExecCodeModuleEx ()
#13 0x00000000004b2b06 in ?? ()
#14 0x00000000004a4ae1 in ?? ()
#15 0x00000000004a45dd in PyImport_ImportModuleLevel ()
#16 0x00000000004a59e4 in ?? ()
#17 0x00000000004a577e in PyObject_Call ()
#18 0x00000000004c5e10 in PyEval_CallObjectWithKeywords ()
#19 0x00000000004be6d7 in PyEval_EvalFrameEx ()
#20 0x00000000004b9ab6 in PyEval_EvalCodeEx ()
#21 0x00000000004b97a6 in PyEval_EvalCode ()
#22 0x00000000004b96df in PyImport_ExecCodeModuleEx ()
#23 0x00000000004b2b06 in ?? ()
#24 0x00000000004a4ae1 in ?? ()
#25 0x00000000004a42c9 in PyImport_ImportModuleLevel ()
#26 0x00000000004a59e4 in ?? ()
#27 0x00000000004a577e in PyObject_Call ()
#28 0x00000000004c5e10 in PyEval_CallObjectWithKeywords ()
#29 0x00000000004be6d7 in PyEval_EvalFrameEx ()
#30 0x00000000004b9ab6 in PyEval_EvalCodeEx ()
#31 0x00000000004b97a6 in PyEval_EvalCode ()
#32 0x00000000004b96df in PyImport_ExecCodeModuleEx ()
#33 0x00000000004b2b06 in ?? ()
#34 0x00000000004a4ae1 in ?? ()
#35 0x00000000004a42c9 in PyImport_ImportModuleLevel ()
#36 0x00000000004a59e4 in ?? ()
#37 0x00000000004a577e in PyObject_Call ()
#38 0x00000000004c5e10 in PyEval_CallObjectWithKeywords ()
---Type <return> to continue, or q <return> to quit---q
Quit
(gdb) 

```

```
(gdb) file python
Reading symbols from python...Reading symbols from /usr/lib/debug/.build-id/66/b65551cc62504bf758e2f57514d33cf3017b8f.debug...done.
done.
f(gdb) run test.py
Starting program: /usr/bin/python test.py
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
warning: Corrupted shared library list: 0xa369d0 != 0xa50dd0

Program received signal SIGSEGV, Segmentation fault.
0x000000000001956e in ?? ()
(gdb) py-bt
Traceback (most recent call first):
  File "/usr/lib/python2.7/socket.py", line 53, in <module>
    import _ssl
  File "/usr/local/lib/python2.7/dist-packages/mysql/connector/network.py", line 33, in <module>
    import socket
  File "/usr/local/lib/python2.7/dist-packages/mysql/connector/connection.py", line 50, in <module>
    from .network import MySQLUnixSocket, MySQLTCPSocket
  File "/usr/local/lib/python2.7/dist-packages/mysql/connector/__init__.py", line 42, in <module>
    from .connection import MySQLConnection
  File "test.py", line 2, in <module>
    import mysql.connector
(gdb) 
```

#### dmesg

```
[170609.968233] python[29162]: segfault at 1956e ip 000000000001956e sp 00007ffede95ff68 error 14 in python2.7[400000+2de000]
[180972.937040] python[6980]: segfault at 1956e ip 000000000001956e sp 00007fffd602c3b8 error 14 in python2.7[400000+2de000]
```

#### 关键信息

```
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
warning: Corrupted shared library list: 0xa369d0 != 0xa50dd0

Program received signal SIGSEGV, Segmentation fault.

```

```
(gdb) py-list
  48    from _socket import *
  49    from functools import partial
  50    from types import MethodType
  51    
  52    try:
 >53        import _ssl
  54    except ImportError:
  55        # no SSL support
  56        pass
  57    else:
  58        def ssl(sock, keyfile=None, certfile=None):
```

