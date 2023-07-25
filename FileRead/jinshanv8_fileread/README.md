# 金山v8任意文件下载
金山 V8 终端安全系统存在任意文件下载漏洞

## 漏洞影响

金山 V8 终端安全系统

## 工具利用

python3 exp.py -u http://127.0.0.1:1111 单个url测试

python3 exp.py -c http://127.0.0.1:1111 cmdshell模式

![exp](./exp.png)

python3 exp.py -f url.txt 批量检测

![poc](./poc.png)

## 免责声明

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。
