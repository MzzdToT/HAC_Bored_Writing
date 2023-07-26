# seeyou_webmail.do_scan
致远oa webmail.do文件泄露敏感信息文件批量扫描poc

## 工具利用

python3 webmail.do_scan.py -u http://127.0.0.1:1111 单个url测试

python3 webmail.do_scan.py -f url.txt 批量检测
会在脚本目录生成存在漏洞的url文件
![exp](./poc.png)


## 免责声明

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。
