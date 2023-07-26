# nginxWebUI runCmd RCE
nginxWebUI runCmd接口未授权访问，导致远程命令执行。

## 工具利用

python3 nginxWebUI_rce.py -u http://127.0.0.1:1111 单个url测试

python3 nginxWebUI_rce.py -f url.txt 批量检测

![](./poc.jpg)

![](./exp.jpg)

## 免责声明

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。
