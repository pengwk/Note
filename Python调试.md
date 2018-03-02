# 调试

分析coredump文件

## Linux动态链接库 调试

LD_DEBUG = [help, all]

http://www.bnikolic.co.uk/blog/linux-ld-debug.html

## 开启

ulimit -c 

ulimit -c unlimited

## 工具

https://wiki.python.org/moin/DebuggingWithGdb

### gdb

info

where bt file run step b r  print c display help

gdb -c core

gdb -p 1000 (pid number)

py-bt

quit q

## 教程

https://stackoverflow.com/questions/29396600/segmentation-fault-core-dump-in-python-c-extension

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

#### 关键信息

[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
warning: Corrupted shared library list: 0xa369d0 != 0xa50dd0

Program received signal SIGSEGV, Segmentation fault.

