# lanhai_rce

蓝海卓越计费管理系统存在rce漏洞，攻击者可执行任意命令。


## 工具利用

python3 lanhai_rce.py -u http://127.0.0.1:1111 单个url测试

python3 lanhai_rce.py -c http://127.0.0.1:1111 cmdshell模式
![exp](./exp.png)

python3 lanhai_rce.py -f url.txt 批量检测

## 免责声明

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。
